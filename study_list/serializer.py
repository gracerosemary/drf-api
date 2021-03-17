from rest_framework import serializers
from .models import StudyList

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'student', 'notes', 'created_at', 'updated_at', 'structure', 'action', 'method')
    model = StudyList