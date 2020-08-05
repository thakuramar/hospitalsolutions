from django.shortcuts import render

from django.views import View


class PatientView(View):

    def get(self, request):

        return render(request, 'patient/about.html')


class NavbarView(View):

    def get(self, request):
        return render(request, 'patient/base.html')


class HomeView(View):

    def get(self, request):
        return render(request, 'patient/index.html')

    #def post(self, request):


