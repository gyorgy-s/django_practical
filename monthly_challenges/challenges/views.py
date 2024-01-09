"""Views for the challenges app.
views here will be called according to the urls.py of this app."""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# Global dictionary for the month:message pairs
challenge = {
    "january": "january message...",
    "february": "february message...",
    "march": "march message...",
    "april": "april message...",
    "may": "may message...",
    "june": "june message...",
    "july": "july message...",
    "august": "august message...",
    "september": "september message...",
    "october": "october message...",
    "november": "november message...",
    "december": "december message...",
}


def home(request):
    list_items = ""
    months = list(challenge.keys())

    for month in months:
        list_items += f"<li><a href='{reverse('month_str', args=[month])}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
    try:
        challenge_text = challenge[month.lower()]
    except KeyError:
        return HttpResponseNotFound("Month not supported.")

    # explicit folder made to diferentiate between templates of a multi app progects
    # using render to return the template directly instead of the two step render_to_string solution
    return render(request, "challenges/challenge.html")


def monthly_challenge_by_number(request, month: int):
    """Redirects to the matching month's monthly_challenge (in str) view."""
    try:
        month_as_str = list(challenge.keys())[month - 1]
    except IndexError:
        return HttpResponseNotFound(f"Month not supported: {month}")
    return HttpResponseRedirect(reverse("month_str", args=[month_as_str]))  # reverse constructs full url, by name set in urls.py
