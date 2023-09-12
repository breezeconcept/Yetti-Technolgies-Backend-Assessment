from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User



# TESTING FOR USER REGISTRATION

class RegistrationTestCase(TestCase):
    def test_registration_form_valid_data(self):
        # Test registration with valid data
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Successful registration should redirect
        self.assertEqual(User.objects.count(), 1)  # Ensure a user account is created

    def test_registration_form_invalid_data(self):
        # Test registration with invalid data
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'invalid-email',  # Invalid email format
            'password1': 'testpassword',
            'password2': 'differentpassword',  # Passwords don't match
        })
        self.assertEqual(response.status_code, 200)  # Registration form should be displayed
        self.assertEqual(User.objects.count(), 0)  # No user account should be created




# TESTING FOR LOGIN AND LOGOUT

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_valid_credentials(self):
        # Test login with valid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Successful login should redirect

    def test_login_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'invalidpassword',  # Incorrect password
        })
        self.assertEqual(response.status_code, 200)  # Login form should be displayed

    def test_logout(self):
        # Test user logout
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Successful logout should redirect



# TESTING TO CHECK FOR AUTHENTICATED USERS

class AccessControlTestCase(TestCase):
    def test_authenticated_user_access(self):
        # Test access to a protected view when logged in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)  # Authenticated user should access the view

    def test_unauthenticated_user_access(self):
        # Test access to a protected view when not logged in
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 302)  # Unauthenticated user should be redirected to login



# TESTING TO CHECK FOR ERROR HANDLING CASES

class ErrorScenariosTestCase(TestCase):
    def test_incorrect_password(self):
        # Test login with incorrect password
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'incorrectpassword',  # Incorrect password
        })
        self.assertEqual(response.status_code, 200)  # Login form should be displayed

    def test_nonexistent_user(self):
        # Test login with a non-existent username
        response = self.client.post(reverse('login'), {
            'username': 'nonexistentuser',  # Non-existent username
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 200)  # Login form should be displayed

