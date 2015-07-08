# -*- coding: utf-8 -*-

from django.db import models
from gallery.models import Item

# Класс категорий верхнего уровня, их должно быть ровно ПЯТЬ!!!
# не больше, и не меньше!!! Менять можно только второй параметр!!!
class Category(models.Model):
    MENU = (
        ('a', r'Для невесты'),
        ('b', r'Для жениха'),
        ('c', r'Для автомобиля'),
        ('d', r'Для детей'),
        ('e', r'Аксессуары'),
    )
    first_menu = models.CharField(verbose_name=r"Верхний уровень меню", max_length=30, choices=MENU)
    name = models.CharField(verbose_name=r"Название", max_length=50, unique=True, )
    slug = models.SlugField(r"Адресная строка", max_length=50, unique=True,
                            help_text=r'Уникальное имя для отображения в адресе(заполнять без пробелов и латиницей)', )
    description = models.TextField(r"Описание", )
    is_active = models.BooleanField(r"Активно", default=True, )
    meta_keywords = models.CharField(r"Ключи", max_length=255,
                                     help_text=r'ключевые слова для СЕО поисковых запросов', )
    meta_description = models.CharField(r"Метатеги", max_length=255,
                                        help_text=r'Метатеги для поиска контента', )
    created_at = models.DateTimeField(r"Создано", auto_now_add=True)
    updated_at = models.DateTimeField(r"Изменено", auto_now=True)
#
    class Meta:
        db_table = r'categories'
        ordering = [r'-created_at', r'first_menu']
        verbose_name = r"Категория"
        verbose_name_plural = r"Категории"

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})

class Product(Item):
    name = models.CharField(verbose_name=r"Наименование", max_length=255, unique=True)
    slug = models.SlugField(verbose_name=r"Адресная строка", max_length=255, unique=True,
                            help_text='Уникальное значение в адресной строки для товара, добавляется автоматически.')
    brand = models.CharField(verbose_name=r"Производитель", max_length=50)
    sku = models.CharField(verbose_name=r"СКЮ", max_length=50)
    price = models.DecimalField(verbose_name=r"Цена", max_digits=9,decimal_places=2)
    old_price = models.DecimalField(verbose_name=r"Старая цена", max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    is_active = models.BooleanField(verbose_name=r"Активно", default=True)
    is_bestseller = models.BooleanField(verbose_name=r"Бестселлер", default=False)
    is_featured = models.BooleanField(verbose_name=r"Распродажа", default=False)
    quantity = models.IntegerField(verbose_name=r"Количество", )
    description = models.TextField(verbose_name=r"Описание", )
    meta_keywords = models.CharField(verbose_name=r"Ключевые слова" ,max_length=255,
                                     help_text='Добавляет ключевые слова в мета-теги странички для СЕО поиска.')
    meta_description = models.CharField(verbose_name=r"Дескрипторы", max_length=255,
                                        help_text='Дескрипторы метатегов')
    created_at = models.DateTimeField(verbose_name=r"Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=r"Изменено", auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = r"Товар"
        verbose_name_plural = r"Товары"

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })

    @property
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


    @property
    def cache_key(self):
        return self.get_absolute_url()
