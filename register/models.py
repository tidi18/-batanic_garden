from django.db import models


class Event(models.Model):
    name_event = models.CharField(max_length=255, blank=False, verbose_name='Название')
    date = models.DateField(blank=False, verbose_name='Дата(-ы) проведения')
    address = models.CharField(max_length=255,  blank=False, verbose_name='Адрес')
    anons = models.TextField(blank=False, verbose_name='Анонс')
    total = models.PositiveIntegerField(default=1200, verbose_name='Общее количество')

    def __str__(self):
        return f'{self.name_event}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Time(models.Model):
    time_choice = (
        ('18:00', '18:00'),
        ('18:30', '18:30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
        ('22:00', '22:00'),
        ('22:30', '22:30'),
        ('23:00', '23:00'),
        ('23:30', '23:30'),
        ('00:00', '00:00'),
        ('00:30', '00:30'),
        ('01:00', '01:00'),
        ('01:30', '01:30'),
        ('02:00', '02:00'),
        ('02:30', '02:30'),
        ('03:00', '03:00'),
        ('03:30', '03:30'),
        ('04:00', '04:00'),
        ('04:30', '04:30'),
        ('05:00', '05:00'),
        ('05:30', '05:30'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.CharField(max_length=5, blank=False, choices=time_choice, verbose_name='Время')
    number_in_the_group = models.PositiveIntegerField(default=2, verbose_name='Количество в группе')

    def __str__(self):
        return f'{self.time}'

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'


class Visitor(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE, verbose_name='Время')
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=False, verbose_name='Фамилия')
    token = models.CharField(max_length=100, blank=True, verbose_name='Токен')

    def __str__(self):
        return f'({self.time}) {self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Посетителя'
        verbose_name_plural = 'Посетители'

