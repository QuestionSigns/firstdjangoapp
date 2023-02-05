from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import Post
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

def hello_world(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'djangoapi/post_list.html', {'posts': posts})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)