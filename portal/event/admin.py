from django.contrib import admin
from django.forms import DateTimeInput

from event.models import EventDetails
from .models import EventDetails
from django.db import models


# Register your models here.
@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ('sl_no', 'club', 'event_name', 'location', 'status', 'updated_time', 'updated_date1')
    fields = ('club', 'event_name','updated_time', 'updated_date1', 'location', 'Registration_link', 'status')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('status',)  # Make status read-only for non-superusers
        return ()
