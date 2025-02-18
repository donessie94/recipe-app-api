"""
Test for models.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

class ModelTest(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successful."""
        dummyEmail = 'dummy@example.com'
        dummyPass = 'dummyPass123'

        #	•get_user_model().objects.create_user(...) creates a user using Django’s custom user model.
	    #   •This is better than directly using User.objects.create_user(...), as get_user_model() ensures it works even if the user model is overridden.
        user = get_user_model().objects.create_user(email=dummyEmail, password=dummyPass)

        self.assertEqual(user.email, dummyEmail)
        self.assertTrue(user.check_password(dummyPass))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        dummyEmails = [ ['test1@EXAMPLE.com', 'test1@example.com'],
                        ['Test2@Example.com', 'Test2@example.com'],
                        ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
                        ['test4@example.COM', 'test4@example.com'],
                        ['test5@ExamPle.Com', 'test5@example.com']
        ]

        #loop trhough the dummyEmail list (email is the first parameter in the element and expectedEmail is the second one)
        #recall this is looping trhough a list of list so this is the python code for this scenario
        for email, expectedEmail in dummyEmails:

            #create an user with the dummyEmails examples (the not normalized ones)
            user = get_user_model().objects.create_user(email=email, password='sample123')

            #check if normalized emails are stored instead of the given ones
            self.assertEqual(user.email, expectedEmail)

    def test_new_user_without_email_error(self):
        """Test creating a user without an email gives us a ValueError."""

        #this code must raise a ValueError, if it does not or raises another kind of error this assert will fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='sample123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(email='test@example.com', password='test123')

        #.is_superuser is a field provided for 'PermissionsMixin' import
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

