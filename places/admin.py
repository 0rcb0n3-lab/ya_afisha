from django.contrib import admin
from places.models import Place, PlaceImage

# Register your models here.
class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
