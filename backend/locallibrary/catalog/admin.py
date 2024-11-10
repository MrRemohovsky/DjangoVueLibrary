from django.contrib import admin
from .models import Genre, Author, Language, Book, BookInstance

admin.site.register(Genre)
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book.author.through
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre', 'language')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'borrower')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'id', 'borrower')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

