from django.urls import path

from appointments.views import ScheduledTimeView

urlpatterns = [
    path("get_available/", ScheduledTimeView.as_view(), name="get_available"),
]
