from django.db import models
from django.utils import timezone
from datetime import timedelta

class Event(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    event_date = models.DateTimeField('Дата и время мероприятия')
    location = models.CharField('Место проведения', max_length=200)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    def __str__(self):
        return self.title
    def time_until_event(self):
        """
        Возвращает оставшееся время до мероприятия
        """
        now = timezone.now()
        if self.event_date > now:
            return self.event_date - now
        return timedelta(0)
    
    def time_until_event_formatted(self):
        """
        Возвращает отформатированное оставшееся время
        """
        time_left = self.time_until_event()
        
        if time_left.total_seconds() <= 0:
            return "Мероприятие уже прошло"
