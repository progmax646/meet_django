from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='meet_index'),
    path('create', views.create, name='meet_create'),
    path('edit', views.edit, name='meet_edit'),
    path('delete', views.delete, name='meet_delete'),
    path('search', views.search, name='meet_search'),
    path('login', views.login_meet, name='meet_login'),
    path('success', views.success_status, name='meet_success'),
    path('logout', views.logout_meet, name='meet_logout'),
    path('edit/reserve/<int:id>', views.get_reserve_page, name='reserve_page'),
    path('edit/reserve', views.edit_reserve, name='reserve'),
    path('get-notification/asd/api', views.search_notification),
    path('find-time-to-meet', views.find_time_to_meet, name='find_time_meet'),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)