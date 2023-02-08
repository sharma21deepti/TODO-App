from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    taskTitle= models.CharField(max_length=50)
    taskDesc=models.CharField(max_length=150)
    time=models.DateTimeField(default=timezone.now)
   

    def _str_(self):
        return self.taskTitle