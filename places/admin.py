from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['image_preview']
    fields = ['image', 'image_preview', 'ordering']

    @admin.display(description='get preview')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height: 200px; width: auto;' />,",
                obj.image.url,
            )
        return 'Нет изображения'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['place', 'ordering', 'image']
    readonly_fields = ['image_preview']

    @admin.display(description='Превью')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto;" />',
                obj.image.url,
            )
        return 'Нет изображения'
