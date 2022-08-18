from django.shortcuts import render
from .models import Student,Teacher, User,Article
from django.db.models import Q
# Create your views here.


def operation(request):
    # It will retrieve all objects
    # student_data = Student.objects.all

    #It will retrieve on limited data with filter
    # student_data =Student.objects.filter(marks=70)

    #It will retrieve excluded data with filter
    # student_data =Student.objects.exclude(marks=70)

    #In order by will retrieve data with asending order/ (-) Desending order /(?) Randomely 
    # student_data =Student.objects.order_by('name')
    # student_data =Student.objects.order_by('-name')
    # student_data =Student.objects.order_by('?')

    #It will retrieve data and it will reverse and slice
    # student_data =Student.objects.order_by('id').reverse()[:5]
    # student_data =Student.objects.order_by('id')[:5]

    #you will get list of dictionaries,/ you can retrieve required field
    # student_data =Student.objects.values()
    # student_data =Student.objects.values('name','city')

    # distinct can be used to target duplicates

    #you will receive data in tuple format
    # student_data =Student.objects.values_list()
    # student_data =Student.objects.values_list('id','name')
    # student_data =Student.objects.values_list('id','name',named=True)

    #to check data based 
    # student_data =Student.objects.using('default')

    # To check with help of datefields like moths/year/day you will get distinct data
    # student_data =Student.objects.dates('pass_date','month')
    # student_data =Student.objects.datetimes(field_name,kind,order='ASC',tzinfo=None)


    # calling none there will be no query excecuted
    # student_data =Student.objects.none()

    ### Second Table 'Teacher' started ### 
    
    # Union performation and both table should have same columns 
    # q1 = Student.objects.values_list('id','name',named=True)
    # q2 = Teacher.objects.values_list('id','name',named=True)
    # student_data = q2.union(q1) #all = True)


    #intersection
    # q1 = Student.objects.values_list('id','name',named=True)
    # q2 = Teacher.objects.values_list('id','name',named=True)
    # student_data = q1.intersection(q2)

    # #difference
    # q1 = Student.objects.values_list('id','name',named=True)
    # q2 = Teacher.objects.values_list('id','name',named=True)
    # student_data = q1.difference(q2)

    #### AND Operators       
    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6,roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    #### OR Operators       
    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    # student_data = Student.objects.filter(Q(id=6) | Q(roll=108))

    #get method used to get unique data/key 
    # student_data = Student.objects.get(id=1)

    # # first will return first element same with last
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').last()

    #It will return latest data
    # student_data = Student.objects.latest('pass_date')


    #It will return earliest data
    # student_data = Student.objects.earliest('pass_date')


    # student_data = Student.objects.all()
    # # print(student_data.exists())

    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    #to create queryset
    # student_data = Student.objects.create(name='Sameer',roll=111,city='Bokaro',marks=60,pass_date='2020-05-04')

    #update the rows
    # student_data = Student.objects.filter(id=11).update(name='Nimish',marks=90)
    # student_data = Student.objects.filter(marks=50).update(city= 'Nagpur')

    # student_data,created = Student.objects.update_or_create(id=11,name='Nimish',defaults={'name':'Che'}) 
    # print(created)

    #Bulk_create

    # obj =[
    #     Student(name='Atif',roll=112,city='Dhanbad',marks=70,pass_date='2020-05-06'),
    #     Student(name='Sahil',roll=113,city='Pune',marks=40,pass_date='2020-06-06'),
    #     Student(name='Kumar',roll=114,city='Dhanbad',marks=30,pass_date='2020-05-06'),
    # ]

    # student_data=Student.objects.bulk_create(obj)

    # retrive data with in bulk
    # student_data=Student.objects.in_bulk([1,2])
    # print(student_data[2].name)
    # student_data=Student.objects.in_bulk([])
    # student_data=Student.objects.in_bulk()


    # to delete student data 
    # student_data=Student.objects.get(pk=14).delete()
    # student_data=Student.objects.all().delete()
    # student_data=Student.objects.filter(marks=40).delete()

    # student_data=Student.objects.all()
    # print(student_data.count())


    # student_data=Student.objects.all()
    # print(student_data.explain()) 


    # student_data =User.objects.select_related('article')
    # for student_datas in student_data:
    #     print(student_datas.article.pub_date)
    # # first_head = student_datas[1]
    # # first_head2 =student_datas[2]
    # print(student_data.query)
    # # print(first_head)
    # # print(first_head2)

    student_data =User.objects.all().prefetch_related('articles')
    # for student_datas in student_data:
    #     print(student_datas.article.pub_date)
    # first_head = student_datas[1]
    # first_head2 =student_datas[2]
    print(student_data.query)
    # print(first_head)
    # print(first_head2)
    










    print('Return:---> ',student_data)
    # print()
    # print('SQL Query:--->',student_data.query)

    return render(request,'school/home.html',{'student':student_data})

