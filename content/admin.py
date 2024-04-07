from django.contrib import admin
from .models import Comment, Blog

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'content_preview', 'created', 'likes')
    readonly_fields = ('created',)
    list_filter = ('blog', 'created')  # Permite filtrar por blog y fecha de creación

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Preview del contenido'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'user', 'created')
    readonly_fields = ('created',)
    search_fields = ('title', 'subtitle', 'content')  # Permite buscar por título, subtítulo y contenido
    list_filter = ('user', 'created')  # Permite filtrar por usuario y fecha de creación

    # Esta función permite editar los comentarios directamente desde el BlogAdmin
    def get_inline_instances(self, request, obj=None):
        if not obj:  # Si estamos creando un nuevo blog, no hay necesidad de mostrar inlines de comentarios.
            return []
        return super().get_inline_instances(request, obj)

class CommentInline(admin.TabularInline):  # O puedes usar admin.StackedInline para un estilo diferente
    model = Comment
    extra = 1  # Cuántos campos de comentarios vacíos mostrar por defecto
    readonly_fields = ('created', 'likes')
    fields = ('user', 'content', 'created', 'likes')

# Agregamos CommentInline a BlogAdmin para poder editar comentarios desde el admin de Blog
BlogAdmin.inlines = [CommentInline]

# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
