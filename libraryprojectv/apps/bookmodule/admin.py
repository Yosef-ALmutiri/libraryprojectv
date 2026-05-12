from django.contrib import admin
from .models import Book, Publisher, Author, Student, Address

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Student)
admin.site.register(Address)