from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import StudyList
from django.urls import reverse_lazy
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class StudyListed(generics.ListCreateAPIView):
    queryset = StudyList.objects.all()
    serializer_class = PostSerializer
    template_name = 'study_list.html'
    model = StudyList

class StudyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyList.objects.all()
    serializer_class = PostSerializer
    template_name = 'study_detail.html'
    # renderer_classes = [TemplateHTMLRenderer]
    model = StudyList 
    fields = ['created_at', 'student', 'structure', 'action', 'method', 'updated_at']
    # success_url = reverse_lazy('study_list')

    # def get(self, request):
    #     queryset = StudyList.objects.all()
    #     return Response({'study_list': queryset})
