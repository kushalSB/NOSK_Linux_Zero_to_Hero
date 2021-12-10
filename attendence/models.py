from django.db import models

import attendence

# Create your models here.
class User (models.Model):
    name= models.CharField(max_length=100)
    semester= models.CharField(max_length=2)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    days_present=models.CharField(max_length=2, default=10)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
        # return [self.name, self.semester, self.phone, self.email]

    def daysPresent(self):
        return self.days_present

   