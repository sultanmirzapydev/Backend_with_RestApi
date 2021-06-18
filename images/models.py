from django.db import models

class Image(models.Model):
	title = models.CharField(max_length=10)
	img_link1 = models.CharField(max_length=300)
	img_link2 = models.CharField(max_length=300)
	img_link3 = models.CharField(max_length=300)
	img_link4 = models.CharField(max_length=300)
	img_link5 = models.CharField(max_length=300)
	img_link6 = models.CharField(max_length=300)
	img_link7 = models.CharField(max_length=300)
	img_link8 = models.CharField(max_length=300)
	img_link9 = models.CharField(max_length=300)
	img_link10 = models.CharField(max_length=300)
	img_link11 = models.CharField(max_length=300)
	img_link12 = models.CharField(max_length=300)
	img_link13 = models.CharField(max_length=300)
	img_link14 = models.CharField(max_length=300)
	img_link15 = models.CharField(max_length=300)
	img_link16 = models.CharField(max_length=300)
	img_link17 = models.CharField(max_length=300)
	img_link18 = models.CharField(max_length=300)
	img_link19 = models.CharField(max_length=300)
	img_link20 = models.CharField(max_length=300)
	added_date = models.DateTimeField(auto_now_add=True)
   
	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class PuppyNames(models.Model):
	owner = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=20)

	def Howmany(self, PuppyNames):
		print(PuppyNames.objects.count())
	def __str__(self):
		return self.name