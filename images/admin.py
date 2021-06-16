from django.contrib import admin
from .models import  Image, PuppyNames, Category

class PuppyAdmin(admin.TabularInline):
	model = PuppyNames
	

class CategoryAdmin(admin.ModelAdmin):
	inlines = [PuppyAdmin]
	
	def totalaf(self,*args, **kwargs):
		return PuppyNames.objects.count()

	list_display = [ 'name','totalaf']


admin.site.register(Category, CategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
	
	
	list_display = ('title', 'id', 'added_date',)
	readonly_fields = ('added_date',)

admin.site.register(Image, ImageAdmin)
