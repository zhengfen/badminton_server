# Generated by Django 3.2.6 on 2021-08-23 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_level_i18n'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['name']},
        ),
    ]
