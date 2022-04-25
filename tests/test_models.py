from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):

    def test_manufacturer_format_str(self):
        format_ = Manufacturer.objects.create(
            name="tests",
            country="tests country"
        )

        self.assertEqual(str(format_), f"{format_.name} {format_.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="driver",
            password="test12345",
            first_name="Test first",
            last_name="Test last"
        )

        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_create_driver_with_license_number(self):
        username = "driver"
        password = "test12345"
        license_number = "QWE12345"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="tests",
            country="tests country"
        )
        car = Car.objects.create(
            model="Test model",
            manufacturer=manufacturer,
        )

        self.assertEqual(str(car), f"{car.model}")
