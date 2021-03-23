from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='meet_index'),
    path('create', views.create, name='meet_create'),
    path('edit', views.edit, name='meet_edit'),
    path('delete', views.delete, name='meet_delete'),
    path('search', views.search, name='meet_search'),
    path('login', views.login_meet, name='meet_login'),
    path('success', views.success_status, name='meet_success'),
    path('logout', views.logout_meet, name='meet_logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)