from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='news/', verbose_name="şəkil seçin")
    blog_title = models.CharField(max_length=200, verbose_name="başlıq")
    blog_description = models.CharField(max_length=200, verbose_name='qisa melumat')
    blog_context = models.TextField(verbose_name="ətraflı məlumat")
    publish_date = models.DateTimeField(auto_now=True, verbose_name="tarix")

    class Meta:
        verbose_name_plural = 'Yeniliklerimiz'

    def __str__(self):
        return self.blog_title
