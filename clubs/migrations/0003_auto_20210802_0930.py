# Generated by Django 3.2.5 on 2021-08-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='club',
            table='clubs',
        ),
        migrations.AlterModelTable(
            name='clubresponsable',
            table='club_responsible',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contacts',
        ),
        migrations.AlterModelTable(
            name='player',
            table='players',
        ),
        migrations.AlterModelTable(
            name='structure',
            table='structures',
        ),
        migrations.AlterModelTable(
            name='team',
            table='teams',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]