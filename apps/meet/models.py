from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Status:
    DURING = 0
    DONE = 1
    REMOVE = 2


class Task_meet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.IntegerField(default=1)
    client_name = models.CharField(max_length=150, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(null=True)
    date_do = models.DateTimeField(null=True)
    status = models.IntegerField()
    notification = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        if self.client_name:
            return self.client_name
        else:
            return f'Зарезервировано {self.id}'

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'