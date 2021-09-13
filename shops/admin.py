from django.contrib import admin

from shops.models import ShopModel, BlogModel, ShopImageModel, TypeModel, CommentModel, ShopCommentModel


class ShopImageStackedInline(admin.StackedInline):
    model = ShopImageModel


@admin.register(ShopModel)
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'long_description', 'discount']
    list_filter = ['created_at']
    readonly_fields = ['real_price']
    inlines = [ShopImageStackedInline]


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'long_description']
    list_filter = ['created_at']


@admin.register(TypeModel)
class TypeModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name', 'created_at']
    list_filter = ['created_at']


@admin.register(ShopCommentModel)
class ShopCommentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name']
    list_filter = ['created_at']
