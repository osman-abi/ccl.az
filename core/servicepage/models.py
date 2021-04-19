from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    service_description = models.CharField(max_length=200)
    service_image = models.ImageField(upload_to='service/')
    context = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title