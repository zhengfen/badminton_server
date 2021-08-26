# Generated by Django 3.2.6 on 2021-08-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20210823_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={},
        ),
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
