from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='userhome'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.view_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('doctor/list/', views.doctor_list, name='doctor_list'),
    path('donors/', views.donor_list, name='donor_list'),
    path("donated_organs/", views.donated_organs_list, name="donated_organs"),


]