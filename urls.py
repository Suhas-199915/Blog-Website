from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.postListView.as_view(), name = 'postList'),
    path('about/', views.aboutView.as_view(), name = 'about'),
    path('post/<int:pk>/', views.postDetailView.as_view(), name = 'postDetail'),
    path('post/new/', views.createPostView.as_view(), name = 'createPost'),
    path('path/<int:pk>/edit/', views.updatePostView.as_view(), name = 'updatePost'),
    path('path/<int:pk>/delete/', views.deletePostView.as_view(), name = 'deletePost'),
    path('post/drafts/', views.draftListView.as_view(), name = 'draftListPost'),
    path('post/<int:pk>/comments/', views.addCommentToPost, name = 'addCommentToPost'),
    path('comment/<int:pk>/approve/', views.commentApprove, name = 'commentApprove'),
    path('comment/<int:pk>/remove/', views.commentDelete, name='commentDelete'),
    path('post/<int:pk>/publish/', views.postPublish, name = 'postPublish'),

]