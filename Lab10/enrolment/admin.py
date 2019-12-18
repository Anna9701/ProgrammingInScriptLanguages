from django.contrib import admin
# Register your models here.

from .models import Student, Lecturer, Lecture
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Lecture)
