# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('application_number', models.CharField(max_length=45, unique=True)),
                ('development_address', models.TextField()),
                ('development_description', models.TextField()),
                ('decision_type', models.TextField()),
                ('registered_date', models.DateField()),
                ('registered_in_last_7_working_days', models.TextField()),
                ('registered_in_last_28_working_days', models.TextField()),
                ('earliest_decision_date', models.DateField()),
                ('decision_date', models.DateField()),
                ('decision_level', models.TextField()),
                ('system_status', models.TextField()),
                ('system_status_change_date', models.DateField()),
                ('applicant_name', models.TextField()),
                ('ward', models.TextField()),
                ('conservation_areas', models.TextField()),
                ('neighbourhood_areas', models.TextField()),
                ('case_officer', models.TextField()),
                ('case_officer_team', models.TextField()),
                ('responsibility_type', models.TextField()),
                ('comment', models.TextField()),
                ('full_application', models.TextField()),
                ('application_type', models.TextField()),
                ('easting', models.IntegerField()),
                ('northing', models.IntegerField()),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=11)),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=11)),
                ('spatial_accuracy', models.TextField()),
                ('last_updated', models.DateField()),
                ('socrata_id', models.IntegerField(unique=True)),
                ('organisation_uri', models.TextField()),
            ],
        ),
    ]
