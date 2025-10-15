from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    @property
    def status(self):
        return "Completed" if self.completed else "Pending"
    
    def __str__(self):
        return self.title