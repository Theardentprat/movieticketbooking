from django.db import models

# Create your models here.
class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self) -> str:
        return self.name