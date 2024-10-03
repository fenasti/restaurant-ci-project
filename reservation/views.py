from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import ReservationContent, ReservationRequest
from .forms import ReservationForm

@login_required
def reservation_page(request):
    """
    Renders the Reservation page
    reservation_display = page content
    ReservationRequest = form 
    """
    # Fetch all reservations content to display
    reservation_display = ReservationContent.objects.all().order_by('-updated_on').first()
    
    # Filter reservations made by the logged-in user
    user_reservations = ReservationRequest.objects.filter(client=request.user)

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
            "reservations": user_reservations,  # Pass only the user's reservations
            "reservation_form": reservation_form,  # Reservation form to be rendered
        },
    )


def reservation_edit(request, reservation_id):
    """
    View to edit reservations
    """
    if request.method == "POST":

        # Get the reservation object by ID
        reservation = get_object_or_404(ReservationRequest, pk=reservation_id)
        reservation_form = ReservationForm(data=request.POST, instance=reservation)

        # Ensure that the reservation belongs to the current logged-in user
        if reservation_form.is_valid() and reservation.client == request.user:
            # Save the updated reservation without committing changes to the DB yet
            reservation = reservation_form.save(commit=False)
            # Optionally, mark it as unapproved after editing if needed
            reservation.approved = False
            reservation.save()  # Save the changes to the DB
            messages.add_message(request, messages.SUCCESS, 'Reservation Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating reservation!')

    return HttpResponseRedirect(reverse('reservation'))