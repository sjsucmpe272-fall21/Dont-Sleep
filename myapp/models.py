from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse("home")


USER_CHOICES = [
    ('driver', 'Driver'),
    ('user', 'User'),

]


class Profile(models.Model):
    Name = models.CharField('Name', max_length=264)
    ContactNo = PhoneNumberField('Contact Number', null=False, blank=False, unique=True)
    RefName = models.CharField('Emergency Contact Name', max_length=264)
    RefContactNo = PhoneNumberField('Emergency Contact Number', null=False, blank=False, unique=True)
    Accuracy = models.IntegerField(default=0)
    no_of_trips = models.IntegerField(default=0)
    no_of_sleeps = models.IntegerField(default=0)
