from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField( verbose_name='Дата создания')

