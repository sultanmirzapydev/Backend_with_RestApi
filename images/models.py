from django.db import models


class TypeOf(models.Model):
	animalType = models.CharField(max_length=10)

	def __str__(self):
		return self.animalType

class Animal(models.Model):
	typeOf = models.ForeignKey(TypeOf, on_delete=models.CASCADE)
	
	name = models.CharField(max_length=20) 
	imgUrl = models.TextField()
	count = models.IntegerField()
	likedCount = models.IntegerField()
	isLiked = models.BooleanField(False)
	price = models.IntegerField()
	offers = models.DecimalField(max_digits=3, decimal_places=2)
	vendorName = models.CharField(max_length=20)


	def __str__(self):
		return self.name





