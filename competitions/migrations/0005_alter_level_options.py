# Generated by Django 3.2.6 on 2021-08-25 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_alter_level_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['id']},
        ),
    ]
