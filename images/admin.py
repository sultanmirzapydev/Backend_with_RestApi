from django.contrib import admin
from .models import TypeOf, Animal, vendorName

class vendorNameAdmin(admin.ModelAdmin):
	model = vendorName
	list_display = ['name', 'id']

admin.site.register(vendorName, vendorNameAdmin )

class AnimalAdmin(admin.TabularInline):
	model = Animal

class AnimalAdminDab( admin.ModelAdmin):
	model = Animal
	list_display = ['name' , 'id','typeOf']

admin.site.register(Animal,AnimalAdminDab)

class TypeOfAdmin(admin.ModelAdmin):
	inlines=[AnimalAdmin]

	list_display = ['animalType', 'id']

admin.site.register(TypeOf, TypeOfAdmin)