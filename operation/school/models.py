from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    empnum = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()


    def __str__(self):
        return self.name







class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    slug = models.CharField(max_length=100)


    def __str__(self):
        return self.headline

    
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE ,related_name='reporter')

    # def __str__(self):
    #     return "%s (%s)" % (
    #         self.first_name,
    #         ", ".join(arti.slug for arti in self.articles.all()),
    #     )