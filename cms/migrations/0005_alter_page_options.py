# Generated by Django 3.2.6 on 2021-08-30 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_page_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'id']},
        ),
    ]
