from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class AdminManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("Email required")
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class Admin(AbstractBaseUser) :
    email=models.EmailField(unique=True)  
    is_active=models.BooleanField(default=True) 

    USERNAME_FIELD='email'
    objects=AdminManager()

    def __str__(self):
        return self.email

class Book(models.Model) :
    title=models.CharField(max_length=200) 
    author=models.CharField(max_length=200) 
    published_date=models.DateField() 

    def __str__(self):
        return self.title
