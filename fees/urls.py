from django.urls import path
from . import views

urlpatterns = [
    path('fpy/', views.f_py),
    path('fdj/', views.f_dj)

]