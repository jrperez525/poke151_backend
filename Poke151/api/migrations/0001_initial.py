# Generated by Django 3.1.2 on 2020-10-08 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=550)),
                ('is_hidden_ability', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'abilities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('dex_number', models.CharField(max_length=3)),
                ('type_one', models.CharField(max_length=10)),
                ('type_two', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'pokemon',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PokemonProfile',
            fields=[
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.pokemon')),
                ('pokedex_entry', models.CharField(max_length=450)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('classification', models.CharField(max_length=25)),
                ('male_ratio', models.CharField(max_length=10)),
                ('female_ratio', models.CharField(max_length=10)),
                ('base_egg_steps', models.CharField(max_length=10)),
                ('base_happiness', models.PositiveSmallIntegerField()),
                ('capture_rate', models.PositiveSmallIntegerField()),
                ('effort_values', models.CharField(max_length=35)),
                ('weakness_normal', models.CharField(max_length=10)),
                ('weakness_fire', models.CharField(max_length=10)),
                ('weakness_water', models.CharField(max_length=10)),
                ('weakness_electric', models.CharField(max_length=10)),
                ('weakness_grass', models.CharField(max_length=10)),
                ('weakness_ice', models.CharField(max_length=10)),
                ('weakness_fight', models.CharField(max_length=10)),
                ('weakness_poison', models.CharField(max_length=10)),
                ('weakness_ground', models.CharField(max_length=10)),
                ('weakness_flying', models.CharField(max_length=10)),
                ('weakness_psychc', models.CharField(max_length=10)),
                ('weakness_bug', models.CharField(max_length=10)),
                ('weakness_rock', models.CharField(max_length=10)),
                ('weakness_ghost', models.CharField(max_length=10)),
                ('weakness_dragon', models.CharField(max_length=10)),
                ('weakness_dark', models.CharField(max_length=10)),
                ('weakness_steel', models.CharField(max_length=10)),
                ('weakness_fairy', models.CharField(max_length=10)),
                ('base_stat_hp', models.PositiveSmallIntegerField()),
                ('base_stat_attack', models.PositiveSmallIntegerField()),
                ('base_stat_defense', models.PositiveSmallIntegerField()),
                ('base_stat_special_attack', models.PositiveSmallIntegerField()),
                ('base_stat_special_defense', models.PositiveSmallIntegerField()),
                ('base_stat_speed', models.PositiveSmallIntegerField()),
                ('base_stat_total', models.PositiveSmallIntegerField()),
                ('ability', models.ManyToManyField(to='api.Ability')),
            ],
            options={
                'ordering': ['pokemon'],
            },
        ),
    ]
