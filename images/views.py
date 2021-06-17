from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ImageSerializer, ImgSearchSerializer,PhotographerSerializer
from .models import Image
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import requests 
#from bs4 import BeautifulSoup as bs4

class ImageListAPIView(generics.ListCreateAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer
	permission_classes = [IsAdminUser]


class ImgGet(APIView):
	serializer_class = ImgSearchSerializer

	def get(self, request):
		queryset = Image.objects.filter(title = 'dog')
		serializer = ImgSearchSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		print(request.data)
		print(request)
		titles = request.data['title']
		print(titles)
		img = Image.objects.filter(title = titles)
		print(img)
		serializer = ImgSearchSerializer(img, many=True)
		return Response({'data': serializer.data})


class ImageSearch(generics.ListAPIView):
	queryset = Image.objects.all()
	serializer_class = ImgSearchSerializer
	filter_backends = [filters.SearchFilter]
	search_fields  = ['title']

# class PhotographerPic(APIView):
# 	##serializer_class = PhotographerSerializer
# 	def post(self, request, *args, **kwargs):
# 		data = request.data
		
# 		#print(data['picId']['id'], data['picId']['picurl'])
# 		URL = data['picId']['picurl']
# 		page = requests.get(URL)

# 		soup = bs4(page.content, 'html5lib')
# 		print(soup.prettify())
# 		imgurl = soup.find_all('img')
# 		print(imgurl)

# 		return Response({'msg': 'lets go'})


# @api_view(['GET', 'POST'])
# def show(request):
# 	if request.method == 'GET':
# 		URL = f'https://unsplash.com/s/photos/dog'
# 		page = requests.get(URL)


# 		soup = bs4(page.content, 'html5lib')
	
# 		img = soup.find_all('img', class_='_2UpQX')[:24]
# 		print((img[:1]))
# 		b = []
# 		for item in img:
# 			a = item['srcset']
# 			b.append(a)
# 		print((b[:1]))
# 		return Response({'data':b})

