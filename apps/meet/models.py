from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Task_meet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'