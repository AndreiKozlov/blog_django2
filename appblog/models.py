from django.db import models


class Category(models.Model): # Таблица категорий в БД
    name = models.CharField('Имя категории', max_length=255) #max_length - макс. 255
    slug = models.SlugField('Url', max_length=255) #ссылка категории (url) сделать в автомате по имени категории!!!

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'