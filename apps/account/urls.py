from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login_account, name='account.login'),
    path('', views.index, name='account.index'),
    path('create', views.create, name='account.create'),
    path('create-order', views.create_order, name='account.create-order'),
    path('order-category/<int:id>', views.order_views, name='account.order'),
    path('order-podcategory/<int:id>/<date>', views.podorder_views, name='account.podorder')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
