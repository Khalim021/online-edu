from django.contrib import admin

from courses.models import CourseModel, CategoryModel, SpeakerModel, SpeakerCommentModel, CourseCommentModel


@admin.register(SpeakerModel)
class SpeakerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']
    search_fields = ['name', 'job']
    list_filter = ['created_at']


@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(SpeakerCommentModel)
class SpeakerCommentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name']
    list_filter = ['created_at']


@admin.register(CourseCommentModel)
class CourseCommentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
    search_fields = ['first_name', 'last_name']
    list_filter = ['created_at']
