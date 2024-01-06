"""Urls for the challenges app.
handles urls for this specific app, routes for this app are rerouted
form the project urls.py (in this case from the "monthly_challenges/urls.py")"""

from django.urls import path

from . import views


urlpatterns = [
    path("january", views.january),
]
