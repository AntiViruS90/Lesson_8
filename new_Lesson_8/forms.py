from django import forms as f
from .models import *


class FormJuice(f.Form):
    my_mas = []
    all = Company.objects.all()
    for a in all:
        my_mas.append((a.id, a.title))
    print(my_mas)
    # firm = f.ModelChoiceField(Product.objects.all())
    # product = f.ModelChoiceField(Product.objects.all())
    firm = f.ModelChoiceField(Company.objects.all(), required=False)
    juice = f.ModelChoiceField(Product.objects.all(), required=False)



class StudentForm(f.Form):
    new_mas = []
    courses = Course.objects.all()
    for course in courses:
        new_mas.append((course.id, course.title))
    student = f.ModelChoiceField(Student.objects.all(), required=False)
    course = f.ModelChoiceField(Course.objects.all(), required=False)


class UserForm(f.Form):
    user = f.ModelChoiceField(User.objects.all())