from django.db import models

class Services(models.Model):
    CATEGORY_CHOICE =[
        ('construction', 'Строительство'),
        ('repair', 'Ремонт'),
        ('design', 'Дизайн'),
        ('enginering', 'Инженерия'),
        ('other', 'Другие виды услуг')
    ]

    name = models.CharField(max_length=200, verbose_name='Наименование услуги')
    description = models.TextField(verbose_name='Описание услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    unit = models.CharField(max_length=200, verbose_name='Единица  измерения', default='м²')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, verbose_name='Категория')
    duration = models.CharField(max_length=100, verbose_name='Сроки выполнения', blank=True)
    is_aviable = models.CharField(max_length=100, verbose_name='Доступность услуги', blank=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
