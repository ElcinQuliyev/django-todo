from django.db import models
from accounts.models import CustomUser


class ChoicesTaskType:
    REWARD_TYPE = [
        ('strength', 'Strength'),
        ('intelligence', 'Intelligence'),
        ('creativity', 'Creativity'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]


class TaskQuestions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    reward_type = models.CharField(max_length=20, choices=ChoicesTaskType.REWARD_TYPE)
    status = models.CharField(
        max_length=20, choices=ChoicesTaskType.STATUS_CHOICES, default='pending'
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
