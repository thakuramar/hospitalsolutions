

from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('doctor/', views.DoctorListView.as_view()),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view()),
    #path('', RedirectView.as_view(url="doctor/")),

    path('about/', views.PatientView.as_view(), name='about'),
    #path('', RedirectView.as_view(url="patient/")),
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),
]
