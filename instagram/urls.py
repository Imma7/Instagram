from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^my-profile/(?P<user_id>\d+)' , views.profile, name = 'profile'),
    url(r'images_profile/(?P<id>\d+)', views.images_profile, name='images_for_profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
