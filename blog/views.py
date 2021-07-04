from datetime import date
from django.http.response import Http404
from django.shortcuts import render

# Create your views here.

blog_posts = [{
    "slug": "the-first-blog",
    "author": "David Ermakov",
    "image": "mountains.jpg",
    "post_title": "The-First-Blog",
    "excerpt": """There's nothing like the views you get when hiking in the mountains! 
        And i wasn't even prepared for what happend whilist i was enjoying the view!""",
    "post_content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, quaerat?
        Possimus, quam saepe? Voluptatem, sunt. Officia possimus cumque
        necessitatibus eos earum iste optio, asperiores sunt doloribus. Iste culpa
        blanditiis porro.
    """,

    "date": date(2021, 7, 21),
},
    {
        "author": "David Ermakov",
        "image": "woods.jpg",
        "slug": "the-secong-blog",
        "post_title": "The Second Blog",
        "excerpt": "This is my second blog, that i would like to share with you",
        "post_content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, quaerat?
        Possimus, quam saepe? Voluptatem, sunt. Officia possimus cumque
        necessitatibus eos earum iste optio, asperiores sunt doloribus. Iste culpa
        blanditiis porro.
    """,
        "date": date(2021, 9, 25),
},
    {
        "author": "David Ermakov",
        "image": "coding.jpg",
        "slug": "the-third-blog",
        "post_title": "The Third Blog",
        "excerpt": "This is my third blog, what i would like to share with you",
        "post_content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore, quaerat?
        Possimus, quam saepe? Voluptatem, sunt. Officia possimus cumque
        necessitatibus eos earum iste optio, asperiores sunt doloribus. Iste culpa
        blanditiis porro.
    """,
        "date": date(2022, 3, 11),
}

]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(blog_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"blogs": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": blog_posts
    })


def blog_post(request, slug):
    try:
        identified_post = next(
            post for post in blog_posts if post['slug'] == slug)
        return render(request, "blog/blog.html", {
            "post": identified_post
        })
    except:
        return Http404()
