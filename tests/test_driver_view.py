from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Driver

DRIVER_URL = reverse("taxi:driver-list")


class PublicDriverTests(TestCase):

    def test_login_required(self):
        response = self.client.get(DRIVER_URL)

        self.assertNotEqual(response, 200)


class PrivateDriverTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tests",
            password="password1234"
        )

        self.client.force_login(self.user)

    def test_retrieve_driver(self):
        Driver.objects.create(
            username="driver",
            first_name="tests name",
            last_name="tests last name",
            password="test123456",
            license_number="QWE12345"
        )

        response = self.client.get(DRIVER_URL)
        driver = Driver.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["driver_list"]),
            list(driver)
        )
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_create_driver(self):
        form_data = {
            "username": "new_user",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "tests first",
            "last_name": "tests last",
            "license_number": "LLL12345"
        }
        self.client.post(reverse("taxi:driver-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.license_number, form_data["license_number"])
