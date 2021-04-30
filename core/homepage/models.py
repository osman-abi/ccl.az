from django.db import models

# Create your models here.



class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    context = models.TextField(blank=True,null=True, verbose_name='qisa mezmun')
    class Meta:
        verbose_name_plural = 'Logo'
    def __str__(self):
        return self.image.url

    
    
class Slide(models.Model):
    image = models.ImageField(
        upload_to='slides/', blank=True, verbose_name='Slayd şəkli')
    context = models.TextField(max_length=80,blank=True,null=True,verbose_name="Slayd mətni")
    button_name = models.CharField(max_length=100, blank=True, verbose_name='Linkin adı')
    button_link = models.URLField(verbose_name='Link')
    class Meta:
        verbose_name_plural = 'Slayd'
    def __str__(self):
        return self.image.url

   
class Support(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    context = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='support/')

    def __str__(self):
        return self.title


class Statistica(models.Model):
    count = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title