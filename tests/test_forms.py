from django.test import TestCase

from taxi.forms import DriverCreateForm, DriverUpdateForm


class FormsTests(TestCase):
    def test_driver_creation_form_with_licence_number_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "tests first",
            "last_name": "tests last",
            "licence_number": "QWE12345"
        }
        form = DriverCreateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_update_form_with_license_number_is_valid(self):
        form_data = {
            "license_number": "QWE12345",
        }
        form = DriverUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
