from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Vehicle


class VehicleAccessControlTests(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='customer_a', password='testpass123')
        self.user_b = User.objects.create_user(username='customer_b', password='testpass123')
        self.vehicle_a = Vehicle.objects.create(owner=self.user_a, make='Toyota', model='Hilux', year=2020)

    def test_owner_can_view_own_vehicle(self):
        self.client.login(username='customer_a', password='testpass123')
        response = self.client.get(reverse('vehicle_detail', args=[self.vehicle_a.id]))
        self.assertEqual(response.status_code, 200)

    def test_other_customer_cannot_view_vehicle(self):
        self.client.login(username='customer_b', password='testpass123')
        response = self.client.get(reverse('vehicle_detail', args=[self.vehicle_a.id]))
        self.assertEqual(response.status_code, 404)

    def test_anonymous_user_redirected_to_login(self):
        response = self.client.get(reverse('vehicle_detail', args=[self.vehicle_a.id]))
        self.assertEqual(response.status_code, 302)