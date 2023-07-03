from django.db import models
from apps.utils.models import TimeStamps
from django.contrib.auth import get_user_model


# Create your models here.
class Task(TimeStamps, models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE())
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
