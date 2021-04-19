from django.db import models

# Create your models here.
class About(models.Model):
    about_image = models.ImageField(upload_to='about/')
    about_title = models.CharField(max_length=100)
    about_context = models.TextField()

    def __str__(self):
        return self.about_title