from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from blog.models import Post
class PostLV(ListView):
    model = Post
    context_object_name = 'posts'