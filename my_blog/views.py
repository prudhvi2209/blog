from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . models import Post
# Create your views here.

class StartingPageView(ListView):
    template_name = "my_blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        queryset= super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name="my_blog/all-posts.html"
    model=Post
    ordering=["-date"]
    context_object_name="all_posts"


class SinglePostView(DetailView):
    template_name="my_blog/post-detail.html"
    model=Post
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["post_tags"]=self.object.tags.all()
        return context
