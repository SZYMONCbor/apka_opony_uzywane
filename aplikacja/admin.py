from django.contrib import admin
from .models import Asortyment



# Register your models here.

@admin.register(Asortyment)
class BookAdmin(admin.ModelAdmin):
    list_display = ['marka', 'bieznik', 'szerokosc', 'profil', 'srednica', 'os', 'glebokosc_bieznika']
    list_filter = ['marka', 'bieznik', 'szerokosc', 'profil', 'srednica', 'os', 'glebokosc_bieznika', 'cena']
    search_fields =['marka', 'bieznik','szerokosc','profil','srednica']

