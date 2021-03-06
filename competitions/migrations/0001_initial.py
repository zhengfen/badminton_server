# Generated by Django 3.2.6 on 2021-08-20 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(null=True)),
                ('turn', models.CharField(blank=True, max_length=100)),
                ('matches_h', models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Home')),
                ('matches_a', models.PositiveIntegerField(blank=True, null=True, verbose_name='Match Away')),
                ('set_h', models.PositiveIntegerField(blank=True, null=True)),
                ('set_a', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'levels',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_h_1', models.PositiveIntegerField(blank=True, null=True)),
                ('score_a_1', models.PositiveIntegerField(blank=True, null=True)),
                ('score_h_2', models.PositiveIntegerField(blank=True, null=True)),
                ('score_a_2', models.PositiveIntegerField(blank=True, null=True)),
                ('score_h_3', models.PositiveIntegerField(blank=True, null=True)),
                ('score_a_3', models.PositiveIntegerField(blank=True, null=True)),
                ('match_h', models.PositiveIntegerField(blank=True, null=True)),
                ('match_a', models.PositiveIntegerField(blank=True, null=True)),
                ('set_h', models.PositiveIntegerField(blank=True, null=True)),
                ('set_a', models.PositiveIntegerField(blank=True, null=True)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.competition')),
                ('player_a', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_away', to=settings.AUTH_USER_MODEL, verbose_name='Player Away')),
                ('player_a2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_away_2', to=settings.AUTH_USER_MODEL)),
                ('player_h', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_home', to=settings.AUTH_USER_MODEL, verbose_name='Player Home')),
                ('player_h2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_home_2', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='competitions.type')),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.AddField(
            model_name='competition',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='competitions.group'),
        ),
        migrations.AddField(
            model_name='competition',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='competitions.level'),
        ),
        migrations.AddField(
            model_name='competition',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_away', to='clubs.team', verbose_name='Team Away'),
        ),
        migrations.AddField(
            model_name='competition',
            name='team_h',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_home', to='clubs.team', verbose_name='Team Home'),
        ),
    ]
