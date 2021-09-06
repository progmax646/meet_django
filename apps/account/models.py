from django.db import models


class Account_category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


class Account_podcategory(models.Model):
    category = models.ForeignKey(Account_category, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегория'


class Color_order(models.Model):
    color = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвета'
        verbose_name_plural = 'Цвет'


class Account_order(models.Model):
    category = models.ForeignKey(Account_category, on_delete=models.CASCADE)
    podcategory = models.ForeignKey(Account_podcategory, on_delete=models.CASCADE, null=True)
    summa = models.IntegerField()
    description = models.CharField(max_length=255)
    date = models.DateField()
    color = models.ForeignKey(Color_order, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расход'


class Account_coming(models.Model):
    category = models.ForeignKey(Account_category, on_delete=models.CASCADE)
    summa = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'Приходы'
        verbose_name_plural = 'Приход'


class Budget(models.Model):
    summa = models.IntegerField()
    category = models.ForeignKey(Account_category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'Бюджеты'
        verbose_name_plural = 'Бюджет'


class Remainder(models.Model):
    category = models.ForeignKey(Account_category, on_delete=models.CASCADE, blank=True)
    date = models.CharField(max_length=255)
    summa = models.IntegerField()

    def __str__(self):
        return self.date
    class Meta:
        verbose_name = 'Остатки'
        verbose_name_plural = 'Остаток'

