from django.contrib import admin
from .models import Recipe,Recipe_Step,Recipe_Img,Recipe_Ingredient
from .forms import RecipeImageForm

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Recipe_Step)
admin.site.register(Recipe_Img)
admin.site.register(Recipe_Ingredient)

# @admin.register(Recipe_Img)
# class CountryAmin(admin.ModelAdmin):
#     form = RecipeImageForm

