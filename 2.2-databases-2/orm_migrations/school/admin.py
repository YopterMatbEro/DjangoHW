from django.contrib import admin

from .models import Student, Teacher


class StudentTeachersRelationInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentTeachersRelationInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
