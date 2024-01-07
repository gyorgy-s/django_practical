"""Urls for the challenges app.
handles urls for this specific app, routes for this app are rerouted
form the project urls.py (in this case from the "monthly_challenges/urls.py")"""

from django.urls import path

from . import views


urlpatterns = [
    # for dynamic urls, the variables are marked with <> in the pattern, these
    # are passed to the matching view as kwarg

    # patterns are checked in order: if the int conversion can be done by_number
    # else it is a str
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
]
