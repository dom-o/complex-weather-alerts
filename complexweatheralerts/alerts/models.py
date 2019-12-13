from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import json
from django.conf import settings

# Create your models here.
class Location(models.Model):
    #Duplicate locations are allowed.
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        constraints=[
            models.CheckConstraint(check=models.Q(latitude__range=(-90, 90)), name='latitude between -90 and 90'),
            models.CheckConstraint(check=models.Q(longitude__range=(-180, 180)), name='longitude between -180 and 180'),
        ]


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db_)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Alert(models.Model):
    activity_name = models.CharField(max_length=500, blank=True)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='alerts', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', related_name='alerts', on_delete=models.CASCADE)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    advance_notice = models.IntegerField()

    class Meta:
        unique_together = ('recipient', 'location')


class Filter(models.Model):
    datapointSchema = json.load(open('/home/domonic/code/complex-weather-alerts/complexweatheralerts/alerts/datapoint.json'))
    WEATHER_OPTION_CHOICES = tuple((k, v['title']) for k,v in datapointSchema['properties'].items())
    COMPARE_OPTION_CHOICES = (
        ('exactly', 'exactly'),
        ('between', 'between'),
        ('more', 'more than'),
        ('less', 'less than'),
        ('enum', 'enum'),
    )

    location = models.ForeignKey('Location', related_name='filters', on_delete=models.CASCADE)
    weather_option = models.CharField(choices=WEATHER_OPTION_CHOICES, max_length=500)
    number = models.DecimalField(max_digits=8, decimal_places=4)
    compare_option = models.CharField(choices=COMPARE_OPTION_CHOICES, max_length=7)
    range = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    #maybe add constraint for if compare option = between range != null??

    class Meta:
        unique_together = ('location', 'weather_option')
        constraints = [
            models.CheckConstraint(
                check=(
                    (~models.Q(compare_option__iexact='between') & models.Q(range__isnull=True)) |
                    (models.Q(compare_option__iexact='between') & models.Q(range__isnull=False))
                ), name='if compare option is between, range is not null')
        ]


# class NumberData(models.Model):
#     COMPARE_OPTION_CHOICES = (
#         ('exactly', 'exactly'),
#         ('between', 'between'),
#         ('more', 'more than'),
#         ('less', 'less than'),
#         ('enum', 'enum'),
#     )
#
#     number = models.DecimalField(max_digits=8, decimal_places=4)
#     compare_option = models.CharField(choices=COMPARE_OPTION_CHOICES, max_length=7)
#     range = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
#     #maybe add constraint for if compare option = between range != null??


# class Filter(models.Model):
#     COMPARE_OPTION_CHOICES = (
#         ('exactly', 'exactly'),
#         ('between', 'between'),
#         ('more', 'more than'),
#         ('less', 'less than')
#     )
#
#     datapointSchema = json.load(open('/home/domonic/code/complex-weather-alerts/complexweatheralerts/alerts/datapoint.json'))
#     WEATHER_OPTION_CHOICES = tuple((k, v['title']) for k,v in datapointSchema['properties'].items())
#
#     location = models.ForeignKey('Location', related_name='filters', on_delete=models.CASCADE)
#     weatherOption = models.CharField(choices=WEATHER_OPTION_CHOICES, max_length=500)
#     stringData = models.TextField(blank=True)
#     numData = models.DecimalField(max_digits=8, decimal_places=4)
#     compareOption = models.CharField(choices=COMPARE_OPTION_CHOICES, max_length=7)
#     range = models.DecimalField(max_digits=8, decimal_places=4)
