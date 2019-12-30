from django.test import TestCase
from django.db import IntegrityError, transaction
from alerts.models import *
from alerts.tasks import *
from alerts.test_data import *

# Create your tests here.
class LocationTest(TestCase):
    def test_latitude_range_constraint(self):
        for (lat, lon) in ((-91,0), (91,0), (-95.354,0), (95.354,0)):
            with self.subTest(lat=lat, lon=lon):
                with transaction.atomic():
                    self.assertRaises(IntegrityError, Location.objects.create, latitude=lat, longitude=lon)
        for (lat,lon) in ((90,0), (-90,0), (0,0), (23.32,0), (-23.32,0)):
            with self.subTest(lat=lat, lon=lon):
                with transaction.atomic():
                    try:
                        Location.objects.create(latitude=lat, longitude=lon)
                    except IntegrityError:
                        self.fail("IntegrityError unexpectedly raised.")

    def test_longitude_range_constraint(self):
        for (lat, lon) in ((0,-181), (0,181), (0,-902.354), (0,902.354)):
            with self.subTest(lat=lat, lon=lon):
                with transaction.atomic():
                    self.assertRaises(IntegrityError, Location.objects.create, latitude=lat, longitude=lon)
        for (lat, lon) in ((0,180), (0,-180), (0,0), (0,103.32), (0,-103.32)):
            with self.subTest(lat=lat, lon=lon):
                try:
                    with transaction.atomic():
                        Location.objects.create(latitude=lat, longitude=lon)
                except IntegrityError:
                    self.fail("IntegrityError unexpectedly raised.")


class FilterTest(TestCase):
    def test_compare_option_and_range_constraint(self):
        data={
            'location':Location.objects.create(latitude=0,longitude=0),
            'weather_option': 'apparentTemperature',
            'number': 60,
        }

        for (compare, range) in (('between', None), ('more', 9)):
            with self.subTest(compare=compare, range=range):
                with transaction.atomic():
                    self.assertRaises(IntegrityError, Filter.objects.create, **data, compare_option=compare, range=range)
        data.pop('location')
        for (compare, range, loc) in (('between', 6, Location.objects.create(latitude=1,longitude=1)), ('more', None, Location.objects.create(latitude=1,longitude=2))):
            with self.subTest(compare=compare, range=range,loc=loc):
                try:
                    with transaction.atomic():
                        Filter.objects.create(**data, location=loc, compare_option=compare, range=range)
                except IntegrityError:
                    self.fail("IntegrityError unexpectedly raised.")


class UserTest(TestCase):
    def test_creation_with_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')

    def test_creation(self):
        #self.assert(User.objects.create_user(email='a@)a.com'))
        pass


class AlertSerializerTest(TestCase):
    pass

class LocationSerializerTest(TestCase):
    pass

class AlertUserTaskTest(TestCase):
    def test_filter_compare(self):
        weather_data = los_angeles_sample_weather_data['daily']['data'][4]
        for filter in compare_test_valid_filters:
            with self.subTest(valid=True,filter=filter, weather_data=weather_data):
                self.assertTrue(compare(filter, weather_data))

        for filter in compare_test_invalid_filters:
            with self.subTest(valid=False,filter=filter, weather_data=weather_data):
                self.assertFalse(compare(filter, weather_data))

#add test to make sure that the the sample weather data schema matches the live api response schema, i.e. that the api schema didn't change without you knowing
