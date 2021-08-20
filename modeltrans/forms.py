import itertools

from django import forms
from django.utils.translation import gettext_lazy as _

from .conf import get_available_languages, get_default_language
from .fields import get_instance_field_value
from .translator import get_i18n_field
from .utils import build_localized_fieldname, get_language

LANGUAGE_OPTIONS = ["browser", "fallback"]


class TranslationModelFormOptions(forms.models.ModelFormOptions):
    """Add the translation form options to the Meta options."""

    def __init__(self, options=None):
        super().__init__(options)
        self.languages = getattr(options, "languages", ["browser", "fallback"])
        self.fallback_language = getattr(options, "fallback_language", None)


class TranslationModelFormMetaClass(forms.models.ModelFormMetaclass):
    def __new__(mcs, name, bases, attrs):
        """
        Include all translation fields for translatable fields declared in the form.

        We use the standard ModelForm field declaration procedure of the ModelFormMetaClass,
        so that all fields are declared during creation of the new object.

        Different actions are required for different Meta class options:
        1) fields - if fields are declared explicitly with the fields option, the related i18n fields will not be
        included, and these have to be added to base_fields.
        2) exclude - if fields are declared implicitly with the exclude option, the i18n translation fields, as well as
        the i18n field itself, will be included. We will remove the i18n field.

        Here all languages are included, so that in the form we can curate which fields are available according to
        settings of the form instance (e.g. kwarg overrides, or model instance fallbacks).
        """
        new_class = super().__new__(mcs, name, bases, attrs)

        # from ModelFormMetaClass, needed for calling fields for model
        base_formfield_callback = None
        for b in bases:
            if hasattr(b, "Meta") and hasattr(b.Meta, "formfield_callback"):
                base_formfield_callback = b.Meta.formfield_callback
                break
        formfield_callback = attrs.pop("formfield_callback", base_formfield_callback)

        # get options, with extra translation form options
        opts = new_class._meta = TranslationModelFormOptions(getattr(new_class, "Meta", None))
        model_class = opts.model

        languages = get_available_languages()

        # Note that base_fields generated by ModelForm do not yet include translation fields if generated with "fields"
        # Meta option, but includes all translation fields if generated with "excludes" Meta option.
        base_fields = list(new_class.base_fields.keys())

        # convert to list in case it is a tuple
        opts_fields = list(opts.fields) if opts.fields else None
        opts_exclude = list(opts.exclude) if opts.exclude else None

        if model_class:
            i18n_field = get_i18n_field(model_class)
            if i18n_field:

                for original_field_name in i18n_field.fields:  # for all translated fields

                    # for all possible system languages
                    for language in languages:
                        field_name = build_localized_fieldname(
                            original_field_name, language, ignore_default=True
                        )

                        # add i18n field if an explicitly chosen field
                        if (
                            opts.fields
                            and original_field_name in base_fields
                            and field_name not in base_fields
                        ):
                            base_fields.append(field_name)
                            opts_fields.append(field_name)

                        # remove field if an explicitly excluded field
                        if (
                            opts.exclude
                            and original_field_name in opts.exclude
                            and field_name in base_fields
                        ):
                            base_fields.remove(field_name)
                            opts_exclude.append(field_name)

                    # Remove the i18n field if present (e.g. because of using the exclude option)
                    name = f"{original_field_name}_i18n"
                    if name in base_fields:
                        base_fields.remove(name)
                    if opts.exclude:
                        opts_exclude.append(name)

                    # Remove the i18n field for the system default language, because that already exists as the default
                    name = f"{original_field_name}_{get_default_language()}"
                    if name in base_fields:
                        base_fields.remove(name)
                    if opts.fields and name in opts.fields:
                        opts_fields.remove(name)
                    if opts.exclude and name not in opts.exclude:
                        opts_exclude.append(name)

                opts.fields = opts_fields
                opts.exclude = opts_exclude

                base_fields = forms.fields_for_model(
                    opts.model,
                    opts.fields,
                    opts.exclude,
                    opts.widgets,
                    formfield_callback,
                    opts.localized_fields,
                    opts.labels,
                    opts.help_texts,
                    opts.error_messages,
                    opts.field_classes,
                    # limit_choices_to will be applied during ModelForm.__init__().
                    apply_limit_choices_to=False,
                )

                # Override default model fields with any custom declared ones
                # (plus, include all the other declared fields).
                base_fields.update(new_class.declared_fields)
            else:
                base_fields = new_class.declared_fields

            # Override base_fields with properly determined set of all translation fields based on ModelForm
            new_class.base_fields = base_fields

        return new_class


class TranslationModelForm(forms.ModelForm, metaclass=TranslationModelFormMetaClass):
    """
    Model form that only adds translation fields for specified languages.

    Meta options and form parameters include:
    - languages: a list defining languages for which translation fields are added.
        - Options are:
            - "browser": current browser language
            - "fallback": the current fallback language, which is the system fallback,
                          or a customized fallback of the translation field.
            - "fr": a language code
        - Overlap is removed, e.g. ["browser", "fr", "fallback"], becomes ["fr"] if all are equal.
        - The list order determines the order of fields in the form.
        - included languages can also be passed via form kwargs to customize on the fly, useful for
          generating translation forms for a specific language.
    - fallback_language: for adapting the fallback language specification on the fly and override the Meta option and/or
    model translation field custom fallback.

    Form parameters take priority of Meta options.

    For the fallback language the following priority holds:
    1) fallback_language passed as form parameter: Form(fallback_language="fr")
    2) the Meta option "fallback_language":
        e.g. Meta:
                fallback_language = "fr"
    3) a custom fallback of a model instance set via "fallback_language_field":
        e.g. i18n = TranslationField(fields=("title", "header"), fallback_language_field="language_code")
    4) The default language of the system. If not Meta option is given fallback reverts to get_default_language()

    Code example:
        class ChallengeModel(models.Model):
            language_code = CharField()
            title = CharField()
            description = CharField()
            i18n = TranslationField(fields=("title", "description"), fallback_language_field="language_code")


        class ChallengeModelForm(RefactoredModelTransForm):

            class Meta:
                fields = ["title", "description"] or exclude = ["language_code"]
                languages = ["browser", "es", "fallback"]


        class ChallengeCreateUpdateView(GenericCreateUpdateView):
            '''An update view with a browser language, spanish and browser field for translations.'''
            model = Challenge
            form_class = ChallengeModelForm()


        class ChallengeTranslationView(GenericCreateUpdateView):
            '''
            A translation view with a specific translation language field and non-editable fallback field as reference.
            '''
            model = Challenge
            form_class = ChallengeModelForm(
                languages=[translation_language_code, "fallback"],
            )
    """

    def __init__(self, *args, languages=None, fallback_language=None, **kwargs):
        """Prune the translation fields based on included languages and fallback_language."""

        self.model_i18n_field = get_i18n_field(self._meta.model)
        self.languages = languages or self._meta.languages
        self.i18n_fields = [
            field for field in self.model_i18n_field.fields if field in self.base_fields.keys()
        ]

        # Given that we set opt.fields and opts.exclude in Meta,
        # the setting of initial values that occurs in ModelForm includes
        # any additional translation fields that have been added in Meta.
        super().__init__(*args, **kwargs)

        # the following require the instance generated in the super call
        self.fallback_language = self.get_fallback_language(fallback_language)
        self.language_codes = self.get_language_codes()
        self.included_fields = self.get_included_fields()

        self.remove_excess_fields()
        self.set_translation_field_attributes()
        self.order_translation_fields()

    def get_included_fields(self):
        """
        Return a dictionary mapping original field names to a list of included field names,
        which may or may not include the original field name.
        """

        fields = {}
        for original_field in self.i18n_fields:
            fields[original_field] = [
                build_localized_fieldname(original_field, language_code, ignore_default=True)
                for language_code in self.language_codes
            ]
        fields["__all__"] = list(itertools.chain.from_iterable(fields.values()))
        return fields

    def set_translation_field_attributes(self):
        """Apply settings of all original field to relevant translation fields."""

        for original_field_name in self.i18n_fields:
            original_field = self.base_fields[original_field_name]
            for field_name in self.included_fields[original_field_name]:
                language = get_default_language()
                if field_name != original_field_name:
                    language = field_name.replace(f"{original_field_name}_", "")
                is_translation = language != self.fallback_language
                label_text = _("translation language") if is_translation else _("default language")
                label = f"{original_field.label} ({language.upper()}, {label_text})"
                self.fields[field_name].label = label
                self.fields[field_name].required = (
                    False if is_translation else original_field.required
                )
                self.fields[field_name].widget = original_field.widget

    def order_translation_fields(self):
        """
        Set the order of the fields, ideally replacing the original field with the set of fields in included fields.

        For the Meta.excludes use a cruder ordering where translated fields types are grouped,
        but per type the languages are in order of: browser, other, fallback
        """

        # Form parameter field_order takes priority, otherwise adopt order of fields in Meta fields option, if available
        field_order = self.field_order or None
        if not field_order and self._meta.fields and self._meta.fields != "all":
            field_order = self._meta.fields

        # in case of an explicit field order replace original field with set of included fields
        if field_order:
            new_field_order = list(field_order)
            for original_field in self.i18n_fields:
                if original_field in new_field_order:
                    index = new_field_order.index(original_field) + 1
                    new_field_order[index:index] = self.included_fields[original_field]
                    new_field_order.pop(index - 1)
            field_order = new_field_order
        else:
            # if no explicit field order adopt the order of i18n form fields used to generate the included fields
            field_order = self.included_fields["__all__"]

        self.order_fields(field_order)

    def remove_excess_fields(self):
        """Remove translations fields that are not included in languages."""
        fields = self.fields.copy()
        for original_field_name in self.i18n_fields:
            for field in fields:
                if original_field_name in field and field not in self.included_fields["__all__"]:
                    self.fields.pop(field)

    def get_fallback_language(self, fallback_language=None):
        """
        Get the fallback language.

        Priority is defined as:
        1) key word argument
        2) form Meta option
        3) model instance custom fallback
        4) system default fallback
        """
        if fallback_language:
            return fallback_language

        if self._meta.fallback_language:
            return self._meta.fallback_language

        if self.model_i18n_field.fallback_language_field and self.instance.pk:
            return get_instance_field_value(
                self.instance, self.model_i18n_field.fallback_language_field
            )

        return get_default_language()

    def get_language_codes(self):
        """Get the languages based on options included in include languages, in the order they are submitted."""

        valid_languages = get_available_languages()
        languages = []
        if self.languages:
            for value in self.languages:
                if value == "browser":
                    value = get_language()
                elif value == "fallback":
                    value = self.fallback_language
                if value not in valid_languages:
                    raise ValueError(f"languages: value {value} is not permitted")
                languages.append(value)

        if not languages:
            raise ValueError("languages: No languages have been defined.")

        # remove duplicates while preserving the order
        no_repeats = set()
        return [x for x in languages if x not in no_repeats and not no_repeats.add(x)]