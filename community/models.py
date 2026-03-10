from django.db import models
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    event_date = models.DateTimeField('Дата и время мероприятия')
    def __str__(self):
        return self.title
