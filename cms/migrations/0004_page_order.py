# Generated by Django 3.2.6 on 2021-08-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_page_on_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
