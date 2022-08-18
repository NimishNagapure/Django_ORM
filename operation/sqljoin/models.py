from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

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