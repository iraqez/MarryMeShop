# -*- coding: utf-8 -*-

from django.db import models

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
    first_menu = models.CharField(max_length=30, choices=MENU)
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

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})
