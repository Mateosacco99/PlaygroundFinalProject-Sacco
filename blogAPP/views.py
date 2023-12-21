from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

def about(request):
    return render(request, "about.html", {})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
