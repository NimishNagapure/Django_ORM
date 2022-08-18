from django.shortcuts import render

from django.shortcuts import render
from .models import Student,Teacher,Book,Store
from django.db import connection
from django.db.models import Q
# Create your views here.




# Simple OR

def student_list(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='Nagapure') | Student.objects.filter(surname__startswith='pk')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='Nimish') | ~Q (surname__startswith='Nagapure') | Q (surname__startswith='cool'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# Simple AND

def student_list_(request):
    posts = Student.objects.filter(classroom=10) & Student.objects.filter(age=4)

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='Nagapure')&Q(firstname__startswith='Nimish'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# Simple UNION

def student_list_(request):

    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})


# Simple EXCLUDE

def student_list_(request):

    posts = Student.objects.exclude(age__gt=19)

    # gt
    # gte
    # lt
    # lte

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})

def student_list_(request):

    posts = Student.objects.filter(~Q(age__gt=20)&~Q(surname__startswith='AP'))

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})


# SELECT & OUTPUT INDIVIDUAL FILEDS

def student_list_(request):

    posts = Student.objects.filter(classroom=1).only('firstname','surname','age')

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'data': posts})


# Simple PERFORMING RAW QUERIES

def student_list_(request):

    # posts = Student.objects.all()

    sql = "SELECT * FROM orm_api_student"
    posts = Student.objects.raw(sql)[:2]

    print(posts)
    #print(connection.queries)
    return render(request,'output.html',{'data': posts})

def student_list_(request):
    post = Student.objects.select_related('teacher')

    for posts in post:
        print(posts)
    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'data': posts})

def student_list_(request):
    books = Book.objects.all().prefetch_related('store_set')
    for book in books:
        print(book.store_set.all())
    print(book)
    print(connection.queries)
    return render(request,'output.html',{'data': book})