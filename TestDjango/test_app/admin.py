from django.contrib import admin
from .models import Testmodel
from .models import Library
from .models import Author
from .models import Magazine
from .models import Book

class CustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname_test', 'lastname_test', 'description')
    list_per_page = 5


admin.site.register(Testmodel, CustomAdmin)


class CustomAdminLibrary(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')


admin.site.register(Library, CustomAdminLibrary)


class CustomAdminAuthor(admin.ModelAdmin):
    list_display = ('first_name_author', 'second_name_author')


admin.site.register(Author, CustomAdminAuthor)


class CustomAdminBook(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Magazine)
admin.site.register(Book)