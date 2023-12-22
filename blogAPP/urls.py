from django.urls import path, include
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, AddCommentView, PagesView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('pages/', PagesView.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('pages/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('pages/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('pages/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('pages/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView, name="Category"),
    


]