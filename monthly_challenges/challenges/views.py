"""Views for the challenges app.
views here will be called according to the urls.py of this app."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# "request" is the base kwarg that is automatically is passed from the url
def january(request):
    """Replaced by dynamic url monthly_challenge."""
    return HttpResponse("January")


def february(request):
    """Replaced by dynamic url monthly_challenge."""
    return HttpResponse("February")


# kwarg is passed from the urls route variable
def monthly_challenge(request, month: str):
    """Displays the message depending on the month, month passed from the url.

    Args:
        request : http request
        month (str): dynamic url var

    Returns:
        HttpResponse: basic str message for the month
    """
    challenge = {
        "january": "january",
        "february": "february",
        "march": "march",
        "april": "april",
        "may": "may",
        "june": "june",
        "july": "july",
        "august": "august",
        "september": "september",
        "october": "october",
        "november": "november",
        "december": "december",
    }
    try:
        message = challenge[month.lower()]
    except KeyError:
        return HttpResponseNotFound("Month not supported.")

    return HttpResponse(message)
