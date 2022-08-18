from django.contrib import admin
from .models import Book ,Store,User,Article

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','price']



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]





@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id' ,'headline', 'pub_date','slug']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id' ,'username' ,'first_name', 'last_name','email']

