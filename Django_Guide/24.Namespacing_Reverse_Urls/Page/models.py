from django.db import models

from django.urls import reverse

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    #file = models.FileField(null=True,blank=True,upload_to='files')
    image = models.ImageField(upload_to='files/img',null=True,blank=True)

    def get_absolute_url(self):
    	return reverse("Page:post-issue", kwargs={"post_id":self.id})



"""
    def get_absolute_url(self):
    	return f"/community/{self.id}/"

"""
