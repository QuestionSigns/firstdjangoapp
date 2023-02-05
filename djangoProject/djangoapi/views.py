from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
import datetime


# Create your views here.
def posts(request):
    response = []
    posts = Post.objects.filter().order_by('-created_date')
    for post in posts: 
        response.append(
            {
                'author': f"{post.user.first_name} {post.user.last_name}" ,
                'title': post.title,
                'text': post.text,
                'publishing_date': post.published_date,
            }
        )

    return JsonResponse(response, safe=False)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'djangoapi/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'djangoapi/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post:Post = form.save(commit=False)
            post.user = request.user
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'djangoapi/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post:Post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'djangoapi/post_edit.html', {'form': form})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
