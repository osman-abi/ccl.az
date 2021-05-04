from django.db import models

# Create your models here.



class Logo(models.Model):
    image = models.ImageField(upload_to='logo/', verbose_name="logo şəkli seçin")
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
    title = models.CharField(max_length=150, verbose_name="başlıq")
    description = models.CharField(max_length=500, verbose_name="qısa məlumat")
    context = models.TextField(blank=True, null=True, verbose_name="ətraflı məlumat")
    image = models.ImageField(upload_to='support/', verbose_name="şəkil")

    class Meta:
        verbose_name_plural = 'Dəstəyimiz'

    def __str__(self):
        return self.title


class Statistica(models.Model):
    count = models.IntegerField(blank=True, null=True, verbose_name="say")
    title = models.CharField(max_length=100, verbose_name="başlıq")

    class Meta:
        verbose_name_plural = "Statistika"

    def __str__(self):
        return self.title