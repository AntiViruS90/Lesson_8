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
    print(firm)


class UserForm(f.Form):
    user = f.ModelChoiceField(User.objects.all())