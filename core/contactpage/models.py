from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    email = models.EmailField(verbose_name="poçt ünvanı")
    phone_number = models.CharField(max_length=50, verbose_name='əlaqə nömrəsi')
    address = models.CharField(max_length=300, verbose_name='ünvan')

    class Meta:
        verbose_name_plural = 'Kontakt Info'
    
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

class ChooseUs(models.Model):
    context = models.TextField(blank=True,null=True,verbose_name="Niyə bizi seçmələri üçün səbəb")
    class Meta:
        verbose_name_plural = 'Niyə biz'
    def __str__(self):
        return self.context

class SubscribedUsers(models.Model):
    email = models.EmailField(verbose_name="poçt ünvanı")
    class Meta:
        verbose_name_plural = 'Yeniliklerden xeberdar olmaq isteyenler'
    def __str__(self):
        return self.email

""" SOCIAL LINKS """

class Facebook(models.Model):
    facebook_link = models.URLField(verbose_name="facebook linki")
    class Meta:
        verbose_name_plural = 'Facebook Link'
    def __str__(self):
        return self.facebook_link

class Instagram(models.Model):
    instagram_link = models.URLField(verbose_name="instagram linki")

    class Meta:
        verbose_name_plural = 'Instagram Link'

    def __str__(self):
        return self.instagram_link


class LinkedIn(models.Model):
    linkedin_link = models.URLField(verbose_name="LinkedIn linki")

    class Meta:
        verbose_name_plural = 'LinkedIn Link'

    def __str__(self):
        return self.linkedin_link


class Whatsapp(models.Model):
    whatsapp_link = models.URLField(verbose_name="whatsapp linki")

    class Meta:
        verbose_name_plural = 'Whatsapp Link'

    def __str__(self):
        return self.whatsapp_link
