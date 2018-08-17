from django.urls import path

from . import views

app_name = 'zine'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('get_post/', views.get_post, name='get_post'),
    path('write_post/', views.write_post, name='write_post'),
    path('posts/<int:pk>/', views.Post_Detail.as_view(), name='post_detail'),
    path('write_comment/<int:post_id>/', views.write_comment, name='write_comment'),
]