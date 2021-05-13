from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'


class ImgSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['img_link1', 'img_link2', 'img_link3', 'img_link4','img_link5','img_link6',
		'img_link7', 'img_link8', 'img_link9', 'img_link10', 'img_link11','img_link12',
		'img_link13', 'img_link14', 'img_link15', 'img_link16', 'img_link17','img_link18',
		'img_link19', 'img_link20']
	

