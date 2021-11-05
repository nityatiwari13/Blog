from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

def frontpage(request):
    posts = Post.objects.all()
    param = {
        'posts' : posts
    }
    return render(request, 'blog/frontpage.html', param)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()        
    param = {
        'post' : post,
        'form' : form
    }
    return render(request, 'blog/post_detail.html', param)
