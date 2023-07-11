from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование')
    product_description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.image} {self.category} ' \
               f'{self.price} {self.date_of_creation} {self.last_modified_date}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
