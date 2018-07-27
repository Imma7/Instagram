from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^my-profile/(?P<profile_id>\d+)' , views.profile, name = 'profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
