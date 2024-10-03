from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ReservationContent, ReservationRequest
from .forms import ReservationForm

def reservation_page(request):
    """
    Renders the Reservation page
    reservation_display = page content
    ReservationRequest = form 
    """
    # Fetch all reservations content to display
    reservation_display = ReservationContent.objects.all().order_by('-updated_on').first()
    
    # Only filter approved reservations (status=1 could represent an 'approved' status)
    # reservations = ReservationRequest.objects.filter(approved=True)

    # Handle form submission
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            # Set the client as the currently logged-in user
            reservation.client = request.user
            reservation.save()
            # Add success message
            messages.add_message(
                request, messages.SUCCESS,
                'Reservation request submitted and awaiting approval'
            )
        else:
            # Add an error message if form is invalid
            messages.add_message(
                request, messages.ERROR,
                'There was an error with your reservation submission. Please try again.'
            )

    else:
        # Initialize the form when the page is accessed via GET
        reservation_form = ReservationForm()

    print("About to render reservation template")

    # Render the template with the reservation list and form
    return render(
        request,
        "reservation/reservation.html",
        {
            "reservation_display": reservation_display,
            "reservation_form": reservation_form,  # Reservation form to be rendered
        },
    )