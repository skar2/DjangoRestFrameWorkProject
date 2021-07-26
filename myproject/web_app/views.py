from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BasicDetails,Education
from .serializers import BasicDetailSerializer,EducationSerializer

class detailslist(APIView):

    def get(self,request):
        details=BasicDetails.objects.all()
        serializer=BasicDetailSerializer(details,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BasicDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class detailsUpdate(APIView):

    def get_object(self,pk):
        try:
            return BasicDetails.objects.get(pk=pk)
        except BasicDetails.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        details=self.get_object(pk)
        serializer=BasicDetailSerializer(details)
        return Response(serializer.data)

    def put(self,request,pk):
        details=self.get_object(pk)
        serializer=BasicDetailSerializer(details,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        details=self.get_object(pk)
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class educationlist(APIView):

    def get(self,request):
        details=Education.objects.all()
        serializer=EducationSerializer(details,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=EducationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class educationUpdate(APIView):

    def get_object(self,pk):
        try:
            return Education.objects.get(pk=pk)
        except Education.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        details=self.get_object(pk)
        serializer=EducationSerializer(details)
        return Response(serializer.data)

    def put(self,request,pk):
        details=self.get_object(pk)
        serializer=EducationSerializer(details,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        details=self.get_object(pk)
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
