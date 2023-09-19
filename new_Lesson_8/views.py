from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')
    pass


def add1(request):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    # prod1 = Product(name='orange', price=140)
    # prod2 = Product(name='apple', price=120)
    # prod3 = Product(name='multy', price=110)
    # comp1 = Company.objects.get(title='J7')
    # comp2 = Company.objects.get(title='DOBRY')
    # comp1.product_set.add(prod1, bulk=False)
    # comp1.product_set.add(prod2, bulk=False)
    # comp1.product_set.add(prod3, bulk=False)
    # comp2.product_set.add(prod1, bulk=False)
    # comp2.product_set.add(prod2, bulk=False)
    # comp2.product_set.add(prod3, bulk=False)
    # print(comp2.product_set.count())
    # print(comp2.product_set.values_list())
    # stud1 = Student.objects.create(name='Mike', group='G001')
    # stud2 = Student.objects.create(name='Tommy', group='G001')
    # stud3 = Student.objects.create(name='John', group='G001')
    # stud4 = Student.objects.create(name='Lisa', group='G002')
    # stud5 = Student.objects.create(name='Ann', group='G002')
    # course1 = Course.objects.create(title='Math')
    # course2 = Course.objects.create(title='Geo')
    # course1.student_set.add(stud1, stud3, stud4, stud5)
    # course2.student_set.add(stud1, stud2, stud3, stud4)
    # user1 = User.objects.create(name='Mike')
    # account1 = Account.objects.create(login='qwer', password='12345', user=user1)
    # user2 = User.objects.create(name='Alice')
    # account2 = Account.objects.create(login='qwerty', password='56789', user=user2)
    return redirect('home')


def table1(request):
    base = Product.objects.all()
    form = FormJuice()
    database = []
    if request.POST:        # Нажали кнопку submit
        form = FormJuice(request.POST)      # Остаются данные с прошлым запросом
        a = request.POST['firm']        # Собираем данные
        b = request.POST['juice']       # Собираем данные
        print(a, b, '==================')
        # Выбираем таблицу для вывода
        if a and not b:     # Если выбран первый вариант, но не второй
            base = Product.objects.filter(firm_id=a)
        elif b and not a:   # Если выбран второй вариант, но не первый
            c = Product.objects.get(id=b).name  # Т.к. id = уникальность, то через .name получаем
            # название продукта и сохраняем в переменную "с"
            base = Product.objects.filter(name=c)
        elif a and b:       # Если выбраны оба варианта
            c = Product.objects.get(id=b).name
            base = Product.objects.filter(firm_id=a, name=c)
        else:               # Если не выбрано ничего, таблица показывает все данные
            base = Product.objects.all()
    for i in base:
        database.append([i.name, i.price, i.firm.title, i.ammount, i.package, i.recommendation])
        # database.append(i.price)
        # database.append(i.firm.title)
    print(database)
    title = ['Name', 'Price', 'Firm', 'Ammount', 'Package', 'Recommendation']   # Строка с заголовком в HTML
    # if request.POST:
    #     a = request.POST['firm']
    #     base = Product.objects.filter(firm_id=a)
    #     for i in base:
    #         database.append([i.name, i.price, i.firm.title])
    context = {'table': database, 'title': title, 'form': form}
    return render(request, 'findTable.html', context=context)   # Вывод данных на страницу HTML
    pass


def table2(request):
    base = Student.objects.all()
    form = StudentForm()
    database = []
    if request.POST:
        form = StudentForm(request.POST)
        student = request.POST['student']
        course = request.POST['course']
        search = {}
        if course:
            search.update({'course': course})
        if student:
            search.update({'id': student})
        base = Student.objects.filter(**search)
    for i in base:
        courses = ', '.join(i.course.values_list('title', flat=True))
        database.append([i.name, i.group, courses])
    title = ['Name', 'Group', 'Course']
    context = {'table': database, 'title': title, 'form': form}
    return render(request, 'findTable.html', context=context)
    pass


def table3(request):
    base = User.objects.all()
    form = UserForm()
    database = []
    if request.POST:
        form = UserForm(request.POST)
        a = request.POST['user']
        base = User.objects.filter(id=a)
    for i in base:
        database.append([i.name, i.account.login, i.account.password])
    title = ['Name', 'Login', 'Password']

    context = {'table': database, 'title': title, 'form': form}
    return render(request, 'findTable.html', context=context)
    pass



def find(request):
    pass
