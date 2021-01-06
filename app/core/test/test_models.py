from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with email is successful.
        """
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        # `assertTrue` is used because password is encrypted.
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized.
        """
        email = 'test@EXAMPLE.COM'
        # added a random string as a password
        # since the password has been alreay tested.
        user = get_user_model().objects.create_user(email, 'testpassword')
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """
        Test creating user with no email raises Error.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword')

    def test_create_new_superuser(self):
        """
        Test creating a new superuser.
        """
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'testpassword'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
