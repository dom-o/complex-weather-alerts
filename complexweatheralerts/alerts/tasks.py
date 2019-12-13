from celery import shared_task
from celery.schedules import crontab
from django.conf import settings
import requests
import json

#for every alert
#   if alert time is valid
    ###if any day in the next 7 days but later than my advance notice threshold is an acceptable day of the week
#       get api data
#       if api data for valid days satisfies filters
#           alert user
@shared_task
def alert_users():
    alerts = Alert.objects.select_related('recipient', 'location').order_by('location')

    current_location = alerts[0].location
    api_location_data = get_location_data(current_location.latitude, current_location.longitude)

    for alert in alerts:
        if(alert.location.latitude != current_location.latitude || alert.location.longitude != current_location.longitude):
            current_location = alert.location
            api_location_data = get_location_data(current_location.latitude, current_location.longitude)

        days = [alert.sunday, alert.monday, alert.tuesday, alert.wednesday, alert.thursday, alert.friday, alert.saturday]

        weather_for_valid_days = [data for data in api_location_data.daily.data if days[datetime.fromtimestamp(data.time).strftime('%w')]]

        filters = alert.location.filter_set.all()

        for weather in weather_for_valid_days:
            valid = compare(filters, weather)
            if valid:
                #alert user
                return


def get_location_data(latitude, longitude):
    url = 'https://api.darksky.net/forecast/{}/{},{}'
    r = requests.get(url.format(settings.DARK_SKY_API_KEY, latitude, longitude), timeout=0.001)
    if r:
        return r.json()
    else:
        r.raise_for_status()


def compare(filters, weather)
    for filter in filters:
        data = weather[filter.weather_option]
        if data == null:
            return False

        if filter.compare_option == "exactly":
            if data == filter.number_data.number:
                return True
        elif filter.compare_option == "between":
            if data <= max(filter.number, filter.range) & data >= min(filter.number, filter.range):
                return True
        elif filter.compare_option == "more":
            if data >= filter.number:
                return True
        elif filter.compare_option == "less":
            if data <= filter.number:
                return True
        elif filter.compare_option == "enum":
            with open('datapoint.json') as file:
                schema = json.load(file)

            if schema.properties[filter.weather_option].enum[filter.enum] == data
                return True
    return False


@shared_task
def add(x, y):
    return x + y
