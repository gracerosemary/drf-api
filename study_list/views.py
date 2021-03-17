from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import StudyList

class StudyListed(generics.ListCreateAPIView):
    queryset = StudyList.objects.all()
    serializer_class = PostSerializer

class StudyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyList.objects.all()
    serializer_class = PostSerializer
