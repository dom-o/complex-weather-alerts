from django.test import TestCase
from django.db import IntegrityError, transaction
from alerts.models import *

# Create your tests here.
class LocationTest(TestCase):
    def test_latitude_range_constraint(self):
        for coord in ((-91,0), (91,0)):
            with self.subTest(coord=coord):
                with transaction.atomic():
                    self.assertRaises(IntegrityError, Location.objects.create, latitude=coord[0], longitude=coord[1])


    def test_longitude_range_constraint(self):
        for coord in ((0,-181), (0,181)):
            with self.subTest(coord=coord):
                with transaction.atomic():
                    self.assertRaises(IntegrityError, Location.objects.create, latitude=coord[0], longitude=coord[1])

class UserTest(TestCase):
    def test_creation_with_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')

    def test_creation(self):
        #self.assert(User.objects.create_user(email='a@)a.com'))
        pass
