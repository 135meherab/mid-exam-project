from django.shortcuts import render, redirect
from car.models import Car
from car.forms import CarForm
from car_brand.models import Brand
from comment.forms import CommentForm
from comment.models import Comment
from django.contrib.auth.decorators import login_required

def home(request, slug_url=None):
    barnds = Brand.objects.all()
    data = Car.objects.all()
    if slug_url is not None:
        b_slug = Brand.objects.get(slug = slug_url)
        data = Car.objects.filter(car_brand = b_slug)
    return render(request, 'home.html', {'data': data, 'brands': barnds})

def details(request, id):
    data = Car.objects.get(pk = id)
    comments = Comment.objects.filter(car = data)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.car = data
            form.save()
            return redirect('home_page')
    else:
        form = CommentForm()
    return render(request, 'details.html', {'data': data, 'form': form, 'comments': comments})

@login_required(login_url='login_page')
def buy(request, id):
    data = Car.objects.get(pk = id)
    data.in_stock -= 1
    data.buyer.add(request.user)
    data.save()
    return redirect('profile_page')
