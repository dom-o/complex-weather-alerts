from rest_framework import serializers
from alerts.models import Location, User, Alert, Filter

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = (
            'id',
            'activityName',
            'recipient',
            'location',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'advanceNotice'
        )

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = (
            'id',
            'location',
            'weatherOption',
            'stringData',
            'numData',
            'compareOption',
            'range'
        )
