from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Category, Link
from .forms import CategoryForm, LinkForm, RegisterForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('category_list')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('category_list')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def category_list(request):
    categories = Category.objects.filter(owner=request.user)
    return render(request, 'category/category_list.html', {'categories':categories})

@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)
        category.owner = request.user
        category.save()
        return redirect('category_list')
    return render(request, 'category/category_form.html', {'form':form})

@login_required
def category_edit(request, id):
    category = get_object_or_404(Category, id=id, owner=request.user)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category/category_form.html', {'form':form})

@login_required
def category_delete(request, id):
    category = get_object_or_404(Category, id=id, owner=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_confirm_delete.html', {'category':category})


@login_required
def category_detail(request, id):
    category = get_object_or_404(Category, id=id, owner=request.user)
    links = category.links.all()
    
    return render(request, 'link/category_detail.html', {'category':category, 'links':links})



# links

@login_required
def link_create(request, category_id):
    category = get_object_or_404(Category, id=category_id, owner=request.user)
    form = LinkForm(request.POST or None)
    if form.is_valid():
        link = form.save(commit=False)
        link.category = category
        link.save()
        return redirect('category_detail', id=category.id)
    return render(request, 'link/link_form.html', {'form':form, 'category':category})

@login_required
def link_edit(request, id):
    link = get_object_or_404(Link, id=id, category__owner=request.user)
    form = LinkForm(request.POST or None, instance=link)
    if form.is_valid():
        form.save()
        return redirect('category_detail', id=link.category.id)
    return render(request, 'link/link_form.html', {'form':form, 'link':link})

@login_required
def link_delete(request, id):
    link = get_object_or_404(Link, id=id, category__owner=request.user)
    if request.method == 'POST':
        link.delete()
        return redirect('category_detail', id=link.category.id)
    return render(request, 'link/link_confirm_delete.html', {'link':link})

