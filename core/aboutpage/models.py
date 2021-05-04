from django.db import models

# Create your models here.
class About(models.Model):
    about_image = models.ImageField(upload_to='about/', verbose_name="şəkil seçin")
    about_title = models.CharField(max_length=100, verbose_name="başlıq")
    about_context = models.TextField(verbose_name="ətraflı məlumat")

    class Meta:
        verbose_name_plural = 'Haqqimizda'

    def __str__(self):
        return self.about_title