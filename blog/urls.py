from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('myposts/', views.my_posts, name='my_posts'),
    path('category/', views.view_posts_by_category, name='view_category'),
    path('blogs/',views.all_post,name="all_post"),
]