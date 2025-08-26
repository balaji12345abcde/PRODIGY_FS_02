from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path
urlpatterns=[
    path('signup/',signupview,name="signup"),
    path('login/',loginview,name="login"),
    path('logout/',logoutview,name="logout"),
    path("employee_list/", employee_list, name="employee_list"),
    path("employee/<int:pk>/", employee_detail, name="employee_detail"),
    path("employee/create/", employee_create, name="employee_create"),
    path("employee/<int:pk>/update/",employee_update, name="employee_update"),
    path("employee/<int:pk>/delete/", employee_delete, name="employee_delete"),
]