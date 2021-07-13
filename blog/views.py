from django.http.response import Http404
from django.shortcuts import render
from .models import Post, Author, Tag

# Create your views here.


blog_postics=Post.objects.all()


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = blog_postics.order_by("-date")
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"blogs": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": blog_postics
    })


def blog_post(request, slug):
    try:
        identified_post = next(
            post for post in blog_postics if post['slug'] == slug)
        return render(request, "blog/blog.html", {
            "post": identified_post
        })
    except:
        return Http404()
