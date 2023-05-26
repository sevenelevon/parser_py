from http.client import HTTPResponse
from rest_framework import generics
from .models import Item
from .serializers import PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = PostSerializer
    
class PostListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = PostSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = PostSerializer