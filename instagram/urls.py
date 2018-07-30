from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^my-profile/(?P<user_id>\d+)' , views.profile, name = 'profile'),
    url(r'images_profile/(?P<id>\d+)', views.images_profile, name='images_for_profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
