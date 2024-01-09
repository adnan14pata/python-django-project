from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    patient = models.BooleanField('patient', default=True)
    doctor = models.BooleanField('doctor', default=True)