from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

# Create your views here.


blog_postics = Post.objects.all()


def starting_page(request):
    sorted_posts = blog_postics.order_by("-date")[:3]
    return render(request, "blog/index.html", {"blogs": sorted_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": blog_postics.order_by("-date")
    })


def blog_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/blog.html", {
        "post": identified_post,
        "tags": identified_post.tags.all()
    })
