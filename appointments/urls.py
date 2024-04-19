from django.urls import path

from appointments.views import ScheduledView

urlpatterns = [
    path("get_scheduled/", ScheduledView.as_view(), name="get_available"),
]
