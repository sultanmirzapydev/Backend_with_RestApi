from django.contrib import admin
from .models import TypweOf, Animals, vendorName


class vendorNameAdmin(admin.ModelAdmin):
	model = vendorName

admin.site.register(vendorName, vendorNameAdmin )

class AnimalAdmin(admin.TabularInline):
	model = Animals

class AnimalAdminDab( admin.ModelAdmin):
	model = Animals

admin.site.register(Animals,AnimalAdminDab)

class TypeOfAdmin(admin.ModelAdmin):
	inlines=[AnimalAdmin]

	list_display = ['animalsType']

admin.site.register(TypweOf, TypeOfAdmin)