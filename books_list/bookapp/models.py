from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30)
    description = models.TextField(max_length=512, blank=True)
    price = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(0)])

    class Meta:
        ordering = ['id']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Profile(models.Model):
    column_name = models.CharField('Название столбца', max_length=30, unique=True) 
    is_visible = models.BooleanField('Флаг видимости столбца', default=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Флаг видимости столбца'
        verbose_name_plural = 'Флаги видимости столбцов'

    def __str__(self):
        return self.column_name
