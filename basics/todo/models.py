from django.db import models


class Task(models.Model):
    title = models.CharField('Task', max_length=100)
    is_complete = models.BooleanField('Is Complete', default=False)
    date = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/todo/'
