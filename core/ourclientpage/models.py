from django.db import models

# Create your models here.
class OurCLients(models.Model):
    client_image = models.ImageField(upload_to='clients/')
    client_title = models.CharField(max_length=200)
    client_description = models.CharField(max_length=200)
    client_context = models.TextField()

    class Meta:
        verbose_name_plural = 'Musterilerimiz'
    
    def __str__(self):
        return self.client_title

        