from django.db import models
# Create your models here.

class List(models.Model):
    user_id = models.ForeignKey()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
