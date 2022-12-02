from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
# Create your models here.
class Thing(models.Model):
    name = models.TextField(unique = True, validators = [MaxLengthValidator(30)], blank = False)
    description = models.TextField(unique = False, validators = [MaxLengthValidator(120)], blank = True)
    quantity = models.IntegerField(
        unique = False,
        validators = [MinValueValidator(0), MaxValueValidator(100)])
