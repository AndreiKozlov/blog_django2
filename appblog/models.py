from django.db import models
from django.utils import timezone
from django.contrib import admin


class Category(models.Model):
    """Таблица категорий в БД"""
    name = models.CharField('Имя категории', max_length=255)
    # ссылка категории (url) сделать в автомате по имени категории!!!
    slug = models.SlugField('Url', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Таблица тегов в БД"""
    name = models.CharField('Имя тега', max_length=60, blank=False)
    slug = models.SlugField('Url', max_length=70, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    """Таблица постов в БД"""
    title = models.CharField('Заголовок поста', max_length=255, blank=False)
    mini_text = models.TextField('Краткое описание', max_length=1024, help_text="Не более 1024 символов", blank=False)
    text = models.TextField('Текст', help_text="Текст поста, без ограничений", blank=False)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата обновления', default=timezone.now)
    slug = models.SlugField('Url', max_length=255, blank=False, unique=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category') связать с категорией

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'created_date') # title заменить на категорию


class Comment(models.Model):
    """Таблица коментариев в БД"""
    text = models.TextField('Коментарий', max_length=1024)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    moderation = models.BooleanField('Проверено модератором', default=False)

    def __str__(self):
        return self.created_date

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'