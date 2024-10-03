from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ReservationContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

class ReservationRequest(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reserver")
    email = models.EmailField()
    details = models.TextField()
    reservation_date_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Reservation request from {self.client.username} on {self.reservation_date_time}"
    