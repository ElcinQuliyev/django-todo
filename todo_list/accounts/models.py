from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # adini deyiw yarrag, User qoy, ozel user yaratmisansa goze soxmamalisan
    avatar_img = models.URLField(max_length=255, blank=True, null=True)
    level = models.PositiveSmallIntegerField(default=0)
    xp = models.PositiveSmallIntegerField(default=0)
    strength = models.PositiveSmallIntegerField(default=10)
    intelligence = models.PositiveSmallIntegerField(default=10)
    creativity = models.PositiveSmallIntegerField(default=10)
    coins = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username
