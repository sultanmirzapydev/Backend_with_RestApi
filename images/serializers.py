from rest_framework import serializers


class  PhotographerSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	url = serializers.CharField(max_length=300)
