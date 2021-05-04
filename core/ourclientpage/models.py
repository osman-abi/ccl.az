from django.db import models

# Create your models here.
class OurCLients(models.Model):
    client_image = models.ImageField(upload_to='clients/', verbose_name="şəkil seçin")
    client_title = models.CharField(max_length=200, verbose_name="başlıq")
    client_description = models.CharField(max_length=200, verbose_name="qısa məlumat")
    client_context = models.TextField(verbose_name="ətraflı məlumat")

    class Meta:
        verbose_name_plural = 'Musterilerimiz'
    
    def __str__(self):
        return self.client_title

class PageImage(models.Model):
    image = models.ImageField(upload_to='our-clients/', verbose_name="şəkil seçin")

    class Meta:
        verbose_name_plural = "'Müştərilərimiz' səhifəsinin ana şəkilləri"

    def __str__(self):
        return self.image