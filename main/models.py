from django.db import models


class Plants(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Название')
    info = models.TextField(blank=False, verbose_name='Информация')
    photo = models.ImageField(upload_to='plants_photo', blank=False, verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'
