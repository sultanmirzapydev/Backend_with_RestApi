from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'


class ImgSearchSerializer(serializers.ModelSerializer):
	#title = serializers.CharField(max_length=10)
	
	class Meta:
		model = Image
		fields = '__all__'
