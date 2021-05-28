from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts, 'section': 'blog'}) 

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=post)
    return render(request,'blog/detail.html',{'post': post})