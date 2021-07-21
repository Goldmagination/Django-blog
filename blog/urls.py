from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsList.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.BlogPostView.as_view(), name="posts-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"), 
]
