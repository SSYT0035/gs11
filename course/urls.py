from django.urls import path
from . import  views
urlpatterns=[
    path('lpy/',views.l_py),
    path('ldj/',views.l_dj)

]