from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    is_patient = models.BooleanField('is patient', default=True)
    is_doctor = models.BooleanField('is doctor', default=True)