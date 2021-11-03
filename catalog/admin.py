from django.contrib import admin
from .models import Author,Book,BookInstance,Genre,Language

# Register your models here.
# Define the admin class

class AuthorInline(admin.TabularInline):
    extra=0
    model=Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields=['first_name','last_name',('date_of_birth','date_of_death')]
    inlines=[AuthorInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
# Register the Admin classes for Book using the decorator

class BookInstanceInline(admin.TabularInline):
    extra=0
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines=[BookInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','borrower', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets= (
        (
            None,{'fields':('book','imprint','id')}
        ),
        ('Availability',{'fields':('status','due_back','borrower')})
    )


