from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SocialMediaPost
from .serializers import SocialMediaPostSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the Social Media Dashboard API</h1>")

class SocialMediaPostList(APIView):
    def get(self, request):
        posts = SocialMediaPost.objects.all()
        serializer = SocialMediaPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SocialMediaPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)