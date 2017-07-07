# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.decorators import api_view

import requests
import os
from rest_framework.response import Response

from planning.models import Planning


@api_view(['POST'])
def update(request):
    response = requests.get('https://opendata.camden.gov.uk/resource/mcgw-i4rx.json')

    for entry in response.json():
        pk = entry.get('pk')
        applicant_name = entry.get('applicant_name', '')
        application_number = entry.get('application_number', '')
        case_officer = entry.get('case_officer', '')
        case_officer_team = entry.get('case_officer_team', '')
        comment = entry.get('comment', '')
        conservation_areas = entry.get('conservation_areas', '')
        decision_date = entry.get('decision_date', None)
        decision_type = entry.get('decision_type', '')
        decision_level = entry.get('decison_level', '')
        development_address = entry.get('development_address', '')
        development_description = entry.get('development_description', '')
        earliest_decision_date = entry.get('earliest_decision_date', None)
        easting = entry['easting']
        northing = entry['northing']
        full_application = entry.get('full_application', '')
        last_updated = entry.get('last_uploaded', None)
        latitude = entry['latitude']
        longitude = entry['longitude']
        organisation_uri = entry.get('organisation_uri', '')
        registered_date = entry.get('registered_date', None)
        registered_in_last_28_days = entry.get('registered_in_last_28_working_days', None)
        registered_in_last_7_days = entry.get('registered_in_last_7_working_days', None)
        responsibility_type = entry.get('responsibility_type', '')
        socrata_id = entry['socrata_id']
        spatial_accuracy = entry.get('spatial_accuracy', '')
        system_status = entry.get('system_status', '')
        system_status_change_date = entry.get('system_status_change_date', None)
        ward = entry.get('ward', '')

        try:
            planning, created = Planning.objects.get_or_create(pk=pk)
            if created:
                continue

            else:
                planning.applicant_name = ascii(applicant_name)
                planning.application_number = ascii(application_number)
                planning.case_officer = ascii(case_officer)
                planning.case_officer_team = ascii(case_officer_team)
                planning.comment = ascii(comment)
                planning.conservation_areas = ascii(conservation_areas)
                planning.decision_date = decision_date
                planning.decision_level = ascii(decision_level)
                planning.decision_type = ascii(decision_type)
                planning.development_address = ascii(development_address)
                planning.development_description = ascii(development_description)
                planning.earliest_decision_date = earliest_decision_date
                planning.easting = easting
                planning.northing = northing
                planning.full_application = ascii(full_application)
                planning.last_updated = last_updated
                planning.latitude = latitude
                planning.longitude = longitude
                planning.registered_date = registered_date
                planning.registered_in_last_7_working_days = registered_in_last_7_days
                planning.registered_in_last_28_working_days = registered_in_last_28_days
                planning.responsibility_type = responsibility_type
                planning.socrata_id = socrata_id
                planning.spatial_accuracy = ascii(spatial_accuracy)
                planning.system_status = system_status
                planning.system_status_change_date = system_status_change_date
                planning.ward = ward
                planning.organisation_uri = ascii(organisation_uri)

                planning.save()

        except Planning.DoesNotExist as e:
            print(e)

        except Exception as e:
            print(e)

    return Response(data="Dataset update completed", status=status.HTTP_200_OK)


@api_view(['GET'])
def show_version(request):
    version = os.getenv("UPDATER_VERSION", "N/A")

    return Response(data=version, status=status.HTTP_200_OK)
