from django.urls import path, re_path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns=[
        path('',views.PostList.as_view(), name = 'index'),
        path('about/',views.AboutView.as_view(), name = 'about'),
        re_path(r'^post/(?P<pk>\d+)/$',views.PostDetail.as_view(), name='post_detail'),
        path('post/new/', views.CreatePost.as_view(), name = 'create_post'),
        re_path(r'^post/(?P<pk>\d+)/edit',views.UpdatePost.as_view(), name = 'update_post'),
        re_path(r'^post/(?P<pk>\d+)/remove', views.DeletePost.as_view(), name = 'delete_post'),
        path('drafts/',views.DraftView.as_view(), name = 'drafts'),
        re_path(r'^post/(?P<pk>\d+)/comment',views.makecomments, name = 'make_comment'),
        re_path(r'^comment/(?P<pk>\d+)/approve',views.approve_comment, name = 'approve_comment'),
        re_path(r'^delete_comment/(?P<pk>\d+)/remove',views.delete_comment, name = 'remove_comment'),
        re_path(r'^post/(?P<pk>\d+)/publish',views.publish_post, name = 'publish'),
        ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
