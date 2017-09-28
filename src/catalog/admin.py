from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
