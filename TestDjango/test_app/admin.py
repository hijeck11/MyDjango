from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Testmodel
from .models import Library
from .models import Author
from .models import Magazine
from .models import Book
from .models import Newspaper
from .models import Article


class CustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname_test', 'lastname_test', 'description')
    list_per_page = 5

admin.site.register(Testmodel, CustomAdmin)

# class Authorinline(admin.TabularInline):
#     model = Author

class CustomAdminLibrary(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


admin.site.register(Library, CustomAdminLibrary)

class Bookinline(admin.TabularInline):
    model = Book
    extra = 1

class Magazineinline(admin.TabularInline):
    model = Magazine
    extra = 1

class CustomAdminAuthor(admin.ModelAdmin):
    list_display = ('first_name_author', 'second_name_author')
    inlines = [Bookinline, Magazineinline]


admin.site.register(Author, CustomAdminAuthor)


class CustomAdminBook(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Magazine)
admin.site.register(Book)
admin.site.register(Newspaper)
admin.site.register(Article)
