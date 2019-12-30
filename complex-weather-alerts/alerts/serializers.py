from rest_framework import serializers
from django.conf import settings
from alerts.models import *


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = (
            'weather_option',
            'number',
            'compare_option',
            'range'
        )


class LocationSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True)

    class Meta:
        model = Location
        fields = (
            'latitude',
            'longitude',
            'filters'
        )

    def create(self, validated_data):
        print(validated_data)
        filters_data = validated_data.pop('filters')
        location = Location.objects.create(**validated_data)
        for filter_data in filters_data:
            filter_data.update({'location': location})
            FilterSerializer.create(FilterSerializer(), validated_data=filter_data)
            #Filter.objects.get_or_create(location=location, **filter_data)
        return location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )


class AlertSerializer(serializers.ModelSerializer):
    recipient = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = Alert
        fields = (
            'activity_name',
            'recipient',
            'location',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'advance_notice',
        )

    def create(self, validated_data):
        user_data = validated_data.pop('recipient')
        location_data = validated_data.pop('location')
        # location,location_created = Location.objects.get_or_create(**location_data)
        # User.objects.get_or_create(email=email)
        # alert,alert_created = Alert.objects.create(**validated_data)
        location = LocationSerializer.create(LocationSerializer(), validated_data=location_data)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        alert = Alert.objects.create(**validated_data, location=location, recipient=user)
        return alert
