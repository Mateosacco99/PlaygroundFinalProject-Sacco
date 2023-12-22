from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

class PagesView(ListView):
    model = Post
    template_name = "pages.html"
    ordering = ["-id"]
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PagesView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-id"]
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

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
    success_url = reverse_lazy("home")

def CategoryView(request, cats):
    category_posts = Post.objects.filter(categoria=cats)
    return render(request, "categories.html", {'cats':cats, 'category_posts':category_posts})

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')
