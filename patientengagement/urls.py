
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/', include('patient.urls')),
    path('', RedirectView.as_view(url="patient/")),

    path('accounts/', include('registration.backends.default.urls')),

]
