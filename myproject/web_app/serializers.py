from rest_framework import serializers
from .models import BasicDetails,Education

class BasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=BasicDetails
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'