from django.db import models

# Create your models here.

class SustainabilityAction(models.Model):
    action = models.CharField(max_length=255)
    date = models.DateField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.date}"