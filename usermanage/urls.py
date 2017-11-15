from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'user/(?P<id>(\d)+)/$',views.show_user, name='show_user'),
    url(r'user_delete/(?P<pk>(\d)+)/$',views.MyUserDelete.as_view(), name='delete_user'),
    url(r'user_update/(?P<pk>(\d)+)/$',views.MyUserUpdate.as_view(), name='update_user'),
    url(r'user_add/$', views.MyUserCreate.as_view(), name="add_user")
]
