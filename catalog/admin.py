from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Define the admin class


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the Admin classes for Book using the decorator
# the @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('display_title', 'id', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('General', {
            'fields': ('book', 'imprint', 'id', 'lang')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# admin.site.register(Author)

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)


# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
