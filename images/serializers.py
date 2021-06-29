from rest_framework import serializers
from models import TypeOf, Animal


class  PhotographerSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	url = serializers.CharField(max_length=300)


class AnimalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Animal 
		fields = ['__all__']

class TypeOfSerializer(serializers.ModelSerializer):
	animal = AnimalSerializer(many=True)

	class Meta:
		model = TypeOf
		fields = ['__all__']