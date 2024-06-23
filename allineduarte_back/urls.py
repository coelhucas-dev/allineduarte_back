from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('clinic/', include('clinics.urls')),
    path('appointment/', include('appointments.urls')),
    path('patient/', include('patients.urls')),
]
