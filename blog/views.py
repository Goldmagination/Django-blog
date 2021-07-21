from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from .models import Post
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


class BlogPostView(View):
    def is_stored_posts(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later= post_id in stored_posts
        else:
            is_saved_for_later=False
        return is_saved_for_later



    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "is_saved_for_later": self.is_stored_posts(request, post.id)
        }

        return render(request, "blog/blog.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment_data=comment_form.save(commit=False)
            comment_data.posts= post
            comment_data.save()
            
            return redirect(reverse("posts-detail-page", args=[slug]))


        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "is_saved_for_later": self.is_stored_posts(request, post.id)
        }
        return render(request, "blog/blog.html", context)
    
class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            context["posts"]=posts
            context["has_posts"]=True
        return render(request, "blog/stored-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts=[]
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts: 
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"]=stored_posts
        return HttpResponseRedirect("/")

    
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
