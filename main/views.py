from django.shortcuts import render, redirect

from item.models import Category, Item 

from .forms import SignupForm, LoginForm



# Create your views here.
def home(request):
    items = Item.objects.filter(is_active=True)[0:6]
    categories = Category.objects.all()


    return render(request,  'index.html', {
        'categories':categories,
        'items': items,
        })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })


def login(request):
    form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })