from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path('api/clinic/', include('clinics.urls')),
    path('api/appointment/', include('appointments.urls')),
    path('api/patient/', include('patients.urls')),
]
