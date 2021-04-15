from django.db import models

# Create your models here.



class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    class Meta:
        verbose_name_plural = 'Logo'
    def __str__(self):
        return self.image.url

    
    
class Slide(models.Model):
    image = models.ImageField(
        upload_to='slides/', blank=True, verbose_name='Slayd şəkli')
    button_name = models.CharField(max_length=100, blank=True, verbose_name='Linkin adı')
    button_link = models.URLField(verbose_name='Link')
    class Meta:
        verbose_name_plural = 'Slayd'
    def __str__(self):
        return self.image.url

   
