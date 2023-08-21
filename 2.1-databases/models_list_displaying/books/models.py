# coding=utf-8

from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Название', max_length=64)
    author = models.CharField('Автор', max_length=64)
    pub_date = models.DateField('Дата публикации', default='1990-01-01')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + self.author
