from django.contrib import admin
from .models import Category, Product, Game, Console


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Game)
admin.site.register(Console)
