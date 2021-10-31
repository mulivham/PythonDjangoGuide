from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def get_absolute_url(self):
    	return f"/community/{self.id}/"