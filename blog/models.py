from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=100)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(blank=True, null=True, auto_now=True, editable=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(max_length=1000, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=CASCADE, null=True, related_name="posts")


    def __str__(self):
        return f"{self.title}, {self.date}"

class Tag(models.Model):
    caption = models.CharField(max_length=10)
    posts = models.ManyToManyField(Post, related_name="tags")

    def __str__(self):
        return f"{self.caption}"


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    text = models.TextField(max_length=300)
    posts = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")