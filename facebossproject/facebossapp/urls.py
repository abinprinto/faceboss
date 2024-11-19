from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('careers/', views.service_details, name='service-details'),
    path('careerdetails/', views.sd, name='sd'),
    path('services/', views.ser, name='ser'),
]