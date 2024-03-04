from django.contrib import admin
from .models import Food, Entry, User, Calorie

# Register your models here.
admin.site.register(Food)
admin.site.register(Entry)
admin.site.register(User)
admin.site.register(Calorie)