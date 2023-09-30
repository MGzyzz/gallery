from django.contrib import admin
from gallery.models import Photo
# Register your models here.
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']



admin.site.register(Photo, PhotosAdmin)
