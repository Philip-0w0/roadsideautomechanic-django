from django.test import TestCase
from django.urls import reverse
from .models import AvailabilitySlot
import datetime


class BookingFormTests(TestCase):
    def setUp(self):
        self.slot = AvailabilitySlot.objects.create(
            date=datetime.date.today() + datetime.timedelta(days=1),
            start_time=datetime.time(10, 0),
            end_time=datetime.time(13, 30),
            max_bookings=1,
        )

    def test_valid_submission_creates_booking(self):
        response = self.client.post(reverse('booking_create'), {
            'customer_name': 'Test User',
            'email': 'test@example.com',
            'phone': '0400000000',
            'vehicle_make': 'Toyota',
            'vehicle_model': 'Hilux',
            'vehicle_year': 2020,
            'service_category': 'General Repairs',
            'description': 'Routine service needed',
            'slot': self.slot.id,
            'consent': True,
            'selected_date': self.slot.date.strftime('%Y-%m-%d'),
        })
        self.assertEqual(response.status_code, 302)

    def test_missing_required_field_shows_error(self):
        response = self.client.post(reverse('booking_create'), {
            'email': 'test@example.com',
        })
        self.assertEqual(response.status_code, 200)