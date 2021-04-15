from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, verbose_name='Əlaqə nömrəsi')
    address = models.CharField(max_length=300, verbose_name='Ünvan')
    
    def __str__(self):
        return self.email

class ContactUs(models.Model):
    username = models.CharField(max_length=200, verbose_name='Istifadəçi adı')
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, verbose_name="İstifadəçinin əlaqə nömrəsi")
    message = models.TextField(verbose_name="İstifadəçi mesajı")

    class Meta:
        verbose_name_plural = 'Əlaqə saxlamaq istəyən istifadəçilər'


    def __str__(self):
        return self.username


""" SOCIAL LINKS """

class Facebook(models.Model):
    facebook_link = models.URLField(verbose_name="facebook linki")
    class Meta:
        verbose_name_plural = 'Facebook Link'
    def __str__(self):
        return self.facebook_link