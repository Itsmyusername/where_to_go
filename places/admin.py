from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html


def image_preview(obj):
    return format_html(
        '<img src="{url}" style="max-height: 200px; max-width: 200px;" />'.format(
            url=obj.img.url
        )
    )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = [image_preview]
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [image_preview]
