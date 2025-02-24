from django.urls import path
from . import views

urlpatterns = [
    path("", views.dochome, name="dochome"),
    path("add_donor/", views.add_donor, name="add_donor"),
    path("viewdonor_list/", views.donor_list, name="viewdonor_list"),
]