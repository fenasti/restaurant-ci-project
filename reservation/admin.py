from django.contrib import admin
from .models import ReservationContent, ReservationRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ReservationContent)
class ReservationAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

admin.site.register(ReservationRequest)