from django.contrib import admin
from .models import Taom
# Register your models here.

@admin.register(Taom)
class TaomAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi', 'mavjudligi', 'kategoriyasi')