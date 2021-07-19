from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Author, Tag
from .forms import CommentForm
# Create your views here.


blog_postics = Post.objects.all()


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "blogs"
    ordering = ["-date"]
    paginate_by = 3

class AllPostsList(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


class BlogPostView(DetailView):
    template_name = "blog/blog.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    
# def starting_page(request):
#     sorted_posts = blog_postics.order_by("-date")[:3]
#     return render(request, "blog/index.html", {"blogs": sorted_posts})


# def posts(request):
#     return render(request, "blog/all-posts.html", {
#         "all_posts": blog_postics.order_by("-date")
#     })


# def blog_post(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/blog.html", {
#         "post": identified_post,
#         "tags": identified_post.tags.all()
#     })
