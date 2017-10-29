from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.post, name='post_list'),
    url(r'^admin_page$', views.admin_page, name='admin_page'),
    url(r'^admin_page/(?P<pk>\d+)/$', views.admin_page, name='admin_page'),
    url(r'^post/new/$', views.displayPost_new, name='displayPost_new'),
    url(r'^post/(?P<pk>\d+)/$', views.work_detail, name='work_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.display_edit, name='display_edit'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
