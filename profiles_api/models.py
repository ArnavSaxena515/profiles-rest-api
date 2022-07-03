import this
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email,name, password=None):
        """Creates a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name) # creates a new object for the entity it is managing. So the userprofilemanager is gonna make a  new instance of user using the user model we have specified and set the email and name for it
        user.set_password(password) # stores the password after passing it through a hash function and stores that hash value, not the actual password in the database
        user.save(using = self._db) #saves user to database. this is the standard way of saving info in db , supports multiple db
        
        return user

    def create_super_user(self,email,name,password):
        """Creates a superuser. Email, name and passwords required"""
        user = self.create_user(email,name,password)

        user.is_admin = True
        user.is_superuser = True # property inherited from PermissionsMixin in our userprofile model
        user.save(using = self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin): #his class inherits from abstractbaseuser and permissionsmixin
    """Database model for users in the system""" # doc string
    email = models.EmailField(max_length=255, unique=True) # creates an email field for the profile with max length 255 and each object's email will have to be unique
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email' # required by default. we tell django that the USERNAME_FIELD it will use for authentication will be the email that the user gives
    REQUIRED_FIELDS = ['name'] # this tells the django admin that name is required

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

        def get_short_name(self):
            """Retrieve short name off user"""
            return self.name

        def __str__(self): # what to do when object converted to string
            """Return string represnetation of our user"""
            return self.email