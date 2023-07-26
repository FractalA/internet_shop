from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Product


def home(request):
    return render(request, 'shop/home.html')


def signupuser(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'shop/signupuser.html', {'form': form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'shop/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'That username has been already taken. '
                                                                         'Choose another one'})

        else:
            return render(request, 'shop/signupuser.html', {'form': UserCreationForm(),
                                                            'error': 'Passwords did not match'})


def show_product(request, product_id):
    return render(request, 'shop/show_product.html', {'product_id': product_id})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/all_products.html', {'products':products})
