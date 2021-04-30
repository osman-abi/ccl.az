from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='news/')
    blog_title = models.CharField(max_length=200)
    blog_description = models.CharField(max_length=200, verbose_name='Qisa melumat')
    blog_context = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Yeniliklerimiz'

    def __str__(self):
        return self.blog_title
