

from django.urls import path
from . import views


urlpatterns = [

    path('about/', views.PatientView.as_view(), name='about'),
    path('', views.NavbarView.as_view(), name='base'),
    path('index/', views.HomeView.as_view(), name='index'),
]
