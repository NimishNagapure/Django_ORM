from django.contrib import admin
from .models import Student, Teacher, Article ,User
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll','city', 'marks','pass_date']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'empnum','city', 'salary','join_date']
     

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id' ,'headline', 'pub_date','slug']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id' ,'username' ,'first_name', 'last_name','email']

