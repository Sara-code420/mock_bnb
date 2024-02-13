from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index), #bnb 
    path('<slug:property_slug>', views.property_details),
]