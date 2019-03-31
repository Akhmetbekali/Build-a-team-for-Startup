from django.test import TestCase
from accounts.forms import RegistrationForm


class MyTests(TestCase):
    def test_forms(self):
        #form_data = {'first_name': 'First', 'last_name': 'Last', 'email': 'Email@innopolis.ru'}
        form_data = {'username': 'username', 'first_name': 'username', 'last_name': 'username',
                     'email': 'username@innopolis.ru', 'password1': '123qwe[]', 'password2': '123qwe[]'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
