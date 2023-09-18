from django.db import models as m


# One to many

class Company(m.Model):
    title = m.CharField(max_length=30)

    def __str__(self):
        return self.title

    pass


class Product(m.Model):
    name = m.CharField(max_length=30)
    price = m.IntegerField()
    firm = m.ForeignKey(Company, on_delete=m.CASCADE)

    def __str__(self):
        return self.name

    pass


# Many - to - many

class Course(m.Model):
    title = m.CharField(max_length=20)

    def __str__(self):
        return self.title


class Student(m.Model):
    name = m.CharField(max_length=50)
    group = m.CharField(max_length=4)
    course = m.ManyToManyField(Course)  # В Database создаёт третью таблицу

    # с ключевыми значениями студент-id и курс-id

    def __str__(self):
        return self.name


# One - to - one


class User(m.Model):
    name = m.CharField(max_length=30)

    def __str__(self):
        return self.name

    pass


class Account(m.Model):
    login = m.CharField(max_length=30)
    password = m.CharField(max_length=30)
    user = m.OneToOneField(User, on_delete=m.CASCADE)
    pass
