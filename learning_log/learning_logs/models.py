from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField

# Create your models here.
class Topic(models.Model):
    """A Topic user is learning about."""

    text = models.CharField(max_length=200)
    date_added = DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text

class Entry(models.Model):

    """Something specific learnt about a Topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) < 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."