# Generated by Django 5.0.3 on 2024-04-09 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_eventdetails_event_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 9, 17, 0, 25, 198820, tzinfo=datetime.timezone.utc)),
        ),
    ]