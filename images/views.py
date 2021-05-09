from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ImageSerializer, ImgSearchSerializer
from .models import Image
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view

class ImageListAPIView(generics.ListCreateAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer
	permission_classes = [IsAdminUser]


class ImgSearch(APIView):
	serializer_class = ImgSearchSerializer

	def get(self, request):
		queryset = Image.objects.all()
		serializer = ImgSearchSerializer(queryset, many=True)
		return Response({'msg':'hello','data': serializer.data})

	def post(self, request, *args, **kwargs):
		if request.data.get('title') != '':
			serializer = ImgSearchSerializer(data=request.data)
			print(serializer)
			if serializer.is_valid():
				serializer.save()
				return Response({
                'success': True,
                'message': 'APIView: post request fulfilled',
                'data': request.data
            })
		

# @api_view(['GET', 'POST'])

# def imgsearch(request):
	
# 	if request.method == 'POST':
# 		return Response({"message": "Got some data!", "data": request.data})
# 	if request.method == 'GET':
# 		return Response({'msg':'success'})

