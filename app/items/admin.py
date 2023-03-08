from django.contrib import admin

from .models import Item, Category, SubCategory, Post
from django.utils.safestring import mark_safe

admin.site.register(Post)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price', 'amount', 'color', 'get_image')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = 'Изображение'
