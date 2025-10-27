from django.contrib import admin
from .models import Upload

admin.site.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display=["uploaded_at"]
# Register your models here.
