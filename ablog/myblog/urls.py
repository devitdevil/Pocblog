
from django.urls import path
from .views import HomeView,ArticleDetailView,AddpostView,AddCategoryView,LikeView,UpdatePostView,DeletePostView,CategoryView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', AddpostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name='delete-post'),
    path('like/<int:pk>', LikeView, name='like_post'),

]









































# path('upvote/<int:pk>', views.upvote, name = "upvote"),
