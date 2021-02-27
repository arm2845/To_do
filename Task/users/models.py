from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", default="image.png")
    phone_number = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.user} {self.phone_number}"

