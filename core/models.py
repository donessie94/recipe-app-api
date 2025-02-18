"""
Database Models.
"""
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):
    """Manager for users."""
    #we can provide any number of keyworkds arguments and they will be passed int our model (**extraFields)
    #example: we could pase 'name' = John and it will populate the field 'name' in the User database for this email
    def create_user(self, email, password=None, **extra_fields):

        #if the value of email is "falsey," (in a boolean context an empty string "" is falsey)
        #we raise a ValueError -> (ValueError is a built-in exceptions so there is no need to import it)
        if not email:
            raise ValueError('The user must have an email adresss.')

        #this creates a new User object basically (because the manager is associated to a model (in our case User, 'self.model' access it))
        #trhough the Django provided function 'normalize_email' we pass the email (so its not like test@ExAmPle.com but instead all lower letters )
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #it encrypts the password with a one way hashing so the database value is some rubbish you cant understand, (functionality provided by django)
        user.set_password(password)

        #supports multiple databases for our project in case is needed (rarely needed tho)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password)

        #for the superuser we define the .is_staff (our custom database field) to be True
        user.is_staff = True

        #this is the automatic field create when migrating our database model definition (Django creates this field automatically, check migrations folder)
        user.is_superuser = True

        #self._db is "default" database from the database configuration in settings.py
        user.save(using=self._db)
        return user

# Create your models here.

#AbstractBaseUser contains the functionality for authentication system
#PermissionsMixin contains permissions and fields fucntionality
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #this is how you assign an user manager in Django
    #'objects' is the default model manager in Django
    objects = UserManager()

    #replace the default username field that comes with the model with 'email' which we will use for uthentification
    USERNAME_FIELD = 'email'
