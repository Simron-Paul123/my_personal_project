# Generated by Django 5.0.3 on 2024-04-09 18:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_eventdetails_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
