from django.db import models


class Articles(models.Model):
    title = models.CharField('Назва:', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата Публікації')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        