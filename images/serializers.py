from rest_framework import serializers
from .models import TypeOf, Animal, vendorName


class  PhotographerSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	url = serializers.CharField(max_length=300)


class VendorNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = vendorName
		fields = ['id','name']

class AnimalSerializer(serializers.ModelSerializer):
	# vendorss =  serializers.CharField(source='vendor',read_only=True)
	vendor = serializers.StringRelatedField()
	class Meta:
		model = Animal 
		fields =['id', 'name', 'imgUrl','count', 'total_liked','isLiked','price', 'offers', 'name', 'vendor']

class TypeOfSerializer(serializers.ModelSerializer):

	typeOf = AnimalSerializer(many=True, read_only=True)
	class Meta:
		model = TypeOf
		fields = ['animalType','typeOf']