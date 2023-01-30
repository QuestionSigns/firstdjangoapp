from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

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
