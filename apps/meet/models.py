from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Task_meet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.IntegerField(default=1)
    client_name = models.CharField(max_length=150, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    date_do = models.DateTimeField(null=True)
    status = models.IntegerField()
    notification = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        if self.client_name:
            return self.client_name
        else:
            return f'Зарезервировано {self.id}'

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'