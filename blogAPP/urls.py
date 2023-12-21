from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', views.about, name="about"),
    path('pages/<int:pk>', ArticleDetailView.as_view(), name="article-detail")

]