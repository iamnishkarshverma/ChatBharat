from django.urls import path, re_path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('delete_post/<uuid:id>/', views.delete_post, name='delete_post'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('help', views.help, name='help'),
    path('helpdata', views.helpdata,name='helpdata'),
    # re_path(r'^share/(?P<post_id>[0-9a-f-]+)$', views.share_post, name='share_post'),

]

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'
