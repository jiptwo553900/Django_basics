from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Intro', max_length=250)
    full_text = models.TextField('Full text')
    date = models.DateTimeField('Date published')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
