"""
Test for Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTest(TestCase):
    """Test for Django admin."""

    #Note: example -> self.admin_user this creates a new instance variable in our class and name it 'admin_user' because
    #in Python like JavaScript you can do all this kind of shit creating instance variables in a class from a function definition
    #BTW: this setUp method creates the dummyUsers we need for our tests
    def setUp(self):
        """Create user and client."""
        #Client is the Django test client wich allow us to make http request
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@example.com', password='sample123')

        #forces the authentification to the self.admin_user
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(email='user@example.com', password='sample123', name='Test User')

    def test_users_list(self):
        """Test that user are listen on page."""

        #this url gets the page that show the list of users
        url = reverse('admin:core_user_changelist')

        #since we are forced to login line 22: "self.client.force_login(self.admin_user)" as the admin user
        #this http request will be made and authenticate by the superuser we created
        #the res object contains the http response to the get(url) request
        res = self.client.get(url)

        #this Django defined assertContains() function checks if in the http response (res) body there exist a 'user.name' and
        #an 'user.email' (wich means in the url where the user list is these fields exist)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""

        #this is the url for the change user page in admin website
        #we need to pass it the specific id for the user we want to change so the url resolves to the specific page we want to
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        #we make sure the response has the status code 200 (OK response)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        #gets the add user url
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

