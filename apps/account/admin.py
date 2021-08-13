from django.contrib import admin
from .models import Account_category, Account_podcategory, Account_coming, Account_order, Budget, Color_order

# Register your models here.
admin.site.register(Account_category)
admin.site.register(Account_podcategory)
admin.site.register(Account_coming)
admin.site.register(Account_order)
admin.site.register(Budget)
admin.site.register(Color_order)