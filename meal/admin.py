from django.contrib import admin
from .models import Taom
from . import models

# Register your models here.

@admin.register(models.Taom)
class TaomAdmin(admin.ModelAdmin):
    list_display = ["nomi", "tavsifi", "narxi"]
    list_editable = ["tavsifi", "narxi"]
    search_fields = ["nomi"]