from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer

CAR_URL = reverse("taxi:car-list")


class PublicCarTests(TestCase):

    def test_login_required(self):
        response = self.client.get(CAR_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCarTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tests",
            password="password1234"
        )

        self.client.force_login(self.user)

    def test_retrieve_car(self):
        manufacturer = Manufacturer.objects.create(
            name="Tesla",
            country="USA"
        )
        Car.objects.create(
            model="tests model",
            manufacturer=manufacturer
        )

        response = self.client.get(CAR_URL)
        car = Car.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["car_list"]),
            list(car)
        )
        self.assertTemplateUsed(response, "taxi/car_list.html")
