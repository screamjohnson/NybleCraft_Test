from django.contrib import admin
from staff.models import Department, Post, Employees


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Department, DepartmentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Post, PostAdmin)


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Employees, EmployeesAdmin)
