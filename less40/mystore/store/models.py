from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    delivery_address = models.TextField()
    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
