from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in admin list view
    list_filter = ('publication_year',)  # Right sidebar filter
    search_fields = ('title', 'author')  # Search bar
