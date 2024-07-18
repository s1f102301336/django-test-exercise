from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    due_at = models.DateTimeField(null=True, blank=True)

    def is_overdue(self, dt):
        if self.due_at is None:
            return False
        return self.due_at < dt
    
class Comment(models.Model):
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
