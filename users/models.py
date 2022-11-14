from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.  
  
class User(AbstractBaseUser, PermissionsMixin):  
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length = 200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_sheikh = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
      
  
  
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name', 'last_name']  
  
    objects = CustomUserManager()  
      
    def has_perm(self, perm, obj=None):  
        "Does the user have a specific permission?"  
        # Simplest possible answer: Yes, always  
        return True  
  
    def is_staff(self):  
        "Is the user a member of staff?"  
        return self.is_staff  
  
    @property  
    def is_admin(self):  
        "Is the user a admin member?"  
        return self.admin 
  
    def __str__(self):  
        return self.email 
        
    
class CustomUserManager(BaseUserManager):  
    def create_user(self, email, password, **extra_fields):  
        """  
        Create and save a User with the given email and password.  
        """  
        if not email:  
            raise ValueError(_('The Email must be set'))  
        email = self.normalize_email(email)  
          
        user = self.model(email=email, **extra_fields)  
        user.set_password(password)  
        user.save()  
        return user  
  
    def create_superuser(self, email, password, **extra_fields):  
        """  
        Create and save a SuperUser with the given email and password.  
        """  
        extra_fields.setdefault('is_staff', True)  
        extra_fields.setdefault('is_superuser', True)  
        extra_fields.setdefault('is_active', True)  
  
        if extra_fields.get('is_staff') is not True:  
            raise ValueError(_('Superuser must have is_staff=True.'))  
        if extra_fields.get('is_superuser') is not True:  
            raise ValueError(_('Superuser must have is_superuser=True.'))  
        return self.create_user(email, password, **extra_fields)  
      
    def get_full_name(self):  
        '''  
        Returns the first_name plus the last_name, with a space in between.  
        '''  
        full_name = '%s %s' % (self.first_name, self.last_name)  
        return full_name.strip()  
  
    def get_short_name(self):  
        '''  
        Returns the short name for the user.  
        '''  
        return self.first_name 

GENDER = [
    ("male", "Male"),
    ("Female", "Female")
]

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
