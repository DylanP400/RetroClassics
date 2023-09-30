from django.contrib import admin
from .models import Category, Product, Game, Console

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Game)
admin.site.register(Console)
