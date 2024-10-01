from django.shortcuts import render
from .models import Reservation


def reservation_page(request):
    """
    Renders the Reservation page
    """
    reservation = Reservation.objects.all()

    return render(
        request,
        "reservation/reservation.html",
        {"reservation": reservation},
    )