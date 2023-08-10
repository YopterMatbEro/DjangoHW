from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Стоимость')
    image = models.CharField(max_length=255)
    release_date = models.DateField(default='2010-01-01', verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=False, verbose_name='4G')
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'name: {self.name}, price: {self.price}'
