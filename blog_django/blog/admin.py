from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'publish')
    sortable_by = ('title', 'writer')
    list_filter = ('writer', 'publish')
    search_fields = ('title', 'writer__username',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('writer',)
