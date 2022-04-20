from django.contrib import admin
from .models import Furniture, Category, Support

# Register your models here.

class FurnitureAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'brand',
        'name',
        'price',
        'condition',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SupportAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )

admin.site.register(Support, SupportAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Category, CategoryAdmin)
