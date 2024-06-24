from django.contrib import admin
from blog.models import leksiya,Rasmlar,Email
@admin.register(leksiya)
class leksiyaAdmin(admin.ModelAdmin):
    list_display = ['nomi']

@admin.register(Rasmlar)
class RasmlarAdmin(admin.ModelAdmin):
    list_display = ['text']
# Register your models here.
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']