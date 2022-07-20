from rest_framework import viewsets
from .models import Post
from serializers import PostSerializer


class PostViewSet(viewsets.Modelviewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


payload = {
    "title": "My first blog post",
    "body": "This is my first blog post"
}

Post.objects.create(title=payload['title'], body=payload['body'])
