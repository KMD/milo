from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'user/(?P<id>(\d)+)/$',views.show_user, name='show_user'),
    url(r'user/add/$', views.MyUserCreate.as_view(), name="add_user")
]
