from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


MAX_IMAGE_HEIGHT = 200
MAX_IMAGE_WIDTH = 200


def get_preview_image(image):
    return format_html(
        '<img src="{url}" style="max-height: {height}px; max-width: {width}px;" />'
        .format(url=image.img.url, height=MAX_IMAGE_HEIGHT, width=MAX_IMAGE_WIDTH)
    )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [get_preview_image]
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ["title"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [get_preview_image]
    autocomplete_fields = ["place"]
