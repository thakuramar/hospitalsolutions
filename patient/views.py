from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from patient.models import Doctor, Patient, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class PatientView(View):

    def get(self, request):

        return render(request, 'about.html')


class NavbarView(View):

    def get(self, request):
        return render(request, 'base.html')


class IndexView(View):

    def get(self, request):

        return render(request, 'index.html')
#def post(self, request):


# it will show the lists  of docter
class DoctorListView(ListView):
    model = Doctor


@method_decorator(login_required, name="dispatch")  # its will not Allow you to enter without log in
class DoctorDetailView(DetailView):  # it will show the full details of docter
    model = Doctor