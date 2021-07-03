
from django.http.response import Http404
from django.shortcuts import render

# Create your views here.

blog_posts = {
    "The First Blog": """There's nothing like the views you get when hiking in the mountains! 
    And i wasn't even prepared for what happend whilist i was enjoying the view!""",
    "The Second Blog": "This is my second blog, that i would like to share with you",
    "The Third Blog": "This is my third blog, what i would like to share with you",
}


def starting_page(reuqest):
    pass


def posts(request):
    return render(request, "blog/index.html", {"blogs": blog_posts})


def blog_post(request, blog_name):
    try:
        blog_content = blog_posts[blog_name]
        return render(request, "blog/blog.html", {
            "blog_name": blog_name,
            "blog_content": blog_content
        })
    except:
        return Http404()
