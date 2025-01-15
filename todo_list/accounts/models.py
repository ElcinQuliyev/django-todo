from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    avatar_img = models.URLField(max_length=255, blank=True, null=True)
    level = models.PositiveSmallIntegerField(default=0)
    xp = models.PositiveSmallIntegerField(default=0)
    strength = models.PositiveSmallIntegerField(default=10)
    intelligence = models.PositiveSmallIntegerField(default=10)
    creativity = models.PositiveSmallIntegerField(default=10)
    coins = models.PositiveSmallIntegerField(default=0)
    