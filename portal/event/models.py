
from django.utils import timezone
from django.db import models

# Create your models here.
class EventDetails(models.Model):
    sl_no = models.AutoField(primary_key=True)
    club = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100,default='')
   # event_date = models.DateField(default=timezone.now)  # Provide a default value here
  #  event_time = models.TimeField()
    location = models.CharField(max_length=100)
    Registration_link = models.URLField(default='https://example.com')
   
    created_date = models.TimeField(auto_now=True)
    updated_time = models.TimeField(default=timezone.now)
    updated_date1 = models.DateField(default=timezone.now)
    status_choices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return str(self.event_name)
   
   


