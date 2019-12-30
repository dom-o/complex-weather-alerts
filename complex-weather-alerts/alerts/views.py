from rest_framework import generics
from alerts.models import Alert
from alerts.serializers import AlertSerializer

# Create your views here.
class AlertList(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    #subscribe user to list
        #this is just a new alert
#----------------

class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    #maybe view to edit alert in addition to subscribe/unsubscribe

    #remove user from list
        #removing an alert
        #must do with auth from user (secret link in email)
#----------------


#add list
    #adding new location, user(?), alert, and filters
        #i guess this is basically just the same as adding a new alert given the
        #serializer we have now; we just expect different things from the data

#get a list
    #need id
    #get alert, location/associated filters, and user(only get user if auth)

#add User
    #currently no reason to add user by themself(?)

#more?????
    #maybe view to edit alert in addition to subscribe/unsubscribe

    #maybe view to edit filters(?)
        #if multiple users are subscribed to list, would just create new list
