from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import CommentForm, PostForm
from django.views.generic import  (TemplateView, ListView,
                                    DetailView, CreateView)
from blog.models import Comment, Post
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_fied_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post
