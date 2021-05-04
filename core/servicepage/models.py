from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="başlıq")
    service_description = models.CharField(max_length=200, verbose_name="qisa məlumat")
    service_image = models.ImageField(upload_to='service/', verbose_name="şəkil seçin")
    context = models.TextField(blank=True,null=True, verbose_name="ətraflı məlumat")

    class Meta:
        verbose_name_plural = 'Xidmetlerimiz'

    def __str__(self):
        return self.title