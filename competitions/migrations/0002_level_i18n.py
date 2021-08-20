# Generated by Django 3.2.6 on 2021-08-20 14:39

from django.db import migrations
import modeltrans.fields


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='i18n',
            field=modeltrans.fields.TranslationField(fields=('name',), required_languages=(), virtual_fields=True),
        ),
    ]
