# Generated by Django 5.0.3 on 2024-04-02 17:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventdetails_registration_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='event_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
