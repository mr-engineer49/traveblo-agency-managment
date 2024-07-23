from django.shortcuts import render, redirect

from item.models import Item 

from .forms import SignupForm, LoginForm

from django.contrib.sessions.models import Session



# Create your views here.
def home(request):
    items = Item.objects.filter(is_active=True)[0:6]

    return render(request,  'index.html', {
        'items': items,
        })


def places(request):
    places = Item.objects.filter(places=True)[0:6]

    return render(request, 'places.html', {
        'places': places,
    })


def restaurants(request):
    restaurants = Item.objects.filter(restaurants=True)[0:6]

    return render(request, 'restaurants.html', {
        'restaurants': restaurants,
    })


def vacations(request):
    vacations = Item.objects.filter(vacations=True)[0:6]

    return render(request, 'vacations.html', {
        'vacations': vacations,
    })


def activities(request):
    activities = Item.objects.filter(activities=True)[0:6]

    return render(request, 'activities.html', {
        'activities': activities,
    })


def trips(request):
    trips = Item.objects.filter(trip=True)[0:6]

    return render(request, 'trip.html', {
        'trips': trips,
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


def logout(request):
    logout = Session.objects.all().delete()
    return render(request, 'index.html', {
        'logout': logout,
    })
