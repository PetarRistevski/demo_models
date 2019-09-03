from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phone = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstName



class UserRole(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role


