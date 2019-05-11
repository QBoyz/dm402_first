from blog.views import PostLV
from django.conf.urls import url

urlpatterns = [
    url(r'^post/$', PostLV.as_view(), name='post_list')
]