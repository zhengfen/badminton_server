# Generated by Django 3.2.6 on 2021-08-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='subject_type',
            field=models.CharField(blank=True, choices=[('Association', 'Association'), ('Club', 'Club')], max_length=255, null=True),
        ),
    ]
