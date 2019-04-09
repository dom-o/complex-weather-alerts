from django.db import models
import json

# Create your models here.
class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class User(models.Model):
    email = models.EmailField(unique=True)

class Alert(models.Model):
    activityName = models.CharField(max_length=500, blank=True)
    recipient = models.ForeignKey('User', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    advanceNotice = models.IntegerField()

    class Meta:
        unique_together = ('recipient', 'location')

class Filter(models.Model):
    COMPARE_OPTION_CHOICES = (
        ('exactly', 'exactly'),
        ('between', 'between'),
        ('more', 'more than'),
        ('less', 'less than')
    )

    datapointSchema = json.load(open('/home/domonic/code/complex-weather-alerts/complexweatheralerts/alerts/datapoint.json'))
    WEATHER_OPTION_CHOICES = tuple((k, v['title']) for k,v in datapointSchema['properties'].items())

    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    weatherOption = models.CharField(choices=WEATHER_OPTION_CHOICES, max_length=500)
    stringData = models.TextField(blank=True)
    numData = models.DecimalField(max_digits=8, decimal_places=4)
    compareOption = models.CharField(choices=COMPARE_OPTION_CHOICES, max_length=7)
    range = models.DecimalField(max_digits=8, decimal_places=4)
