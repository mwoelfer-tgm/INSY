from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.index),
    url(r'details/(?P<aid>[0-9]+)/$', views.details, name="details"),
]
