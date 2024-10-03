from .models import ReservationRequest
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationRequest
        fields = ('client', 'email', 'details', 'reservation_date_time')