from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from alerts import views
#this is alerts/urls
urlpatterns = [
    path('alerts', views.AlertList.as_view()),
    path('alerts/<int:pk>/', views.AlertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
