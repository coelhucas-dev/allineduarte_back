from django.urls import path

from appointments.views import AppointmentCreateView, ScheduledView

urlpatterns = [
    path("get_scheduled/", ScheduledView.as_view(), name="get_available"),
    path('schedule/', AppointmentCreateView.as_view(), name='schedule')
]
