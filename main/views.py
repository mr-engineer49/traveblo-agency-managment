from django.shortcuts import render, redirect
<<<<<<< HEAD
from item.models import Item 
from .forms import SignupForm, LoginForm
from django.contrib.sessions.models import Session
import requests

def home(request):
    items = Item.objects.all()[0:6]

    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"
    querystring = {
        "latitude": "19.24232736426361",
        "longitude": "72.85841985686734",
        "adults": "1",
        "children_age": "0,17",
        "room_qty": "1",
        "units": "metric",
        "page_number": "1",
        "temperature_unit": "c",
        "languagecode": "en-us",
        "currency_code": "EUR"
    }
    headers = {
        'x-rapidapi-key': "8862551c8amshc0fc1ea14ce02bep17600ejsna25133797fa5",
        'x-rapidapi-host': "booking-com15.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        booking_data = response.json()
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        booking_data = {}
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        booking_data = {}

    # Debug print to inspect the data structure of booking_data
    print(f"Booking data: {booking_data}")

    latest_booking = booking_data.get('result', [])

    # Debug print to inspect the structure of latest_booking
    print(f"Latest booking data: {latest_booking}")

    review_score_word = []
    city_in_trans = []
    city = []
    unit_configuration_label = []
    hotel_name_trans = []
    min_total_price = []
    hotel_name = []
    main_photo_url = []

    for booking in latest_booking:
        review_score_word.append(booking.get('review_score_word'))
        city_in_trans.append(booking.get('city_in_trans'))
        city.append(booking.get('city'))
        unit_configuration_label.append(booking.get('unit_configuration_label'))
        hotel_name_trans.append(booking.get('hotel_name_trans'))
        min_total_price.append(booking.get('min_total_price'))
        hotel_name.append(booking.get('hotel_name'))
        main_photo_url.append(booking.get('main_photo_url'))

    context = {
        'items': items,
        'latest_booking': latest_booking,
        'review_score_word': review_score_word,
        'city_in_trans': city_in_trans,
        'city': city,
        'unit_configuration_label': unit_configuration_label,
        'hotel_name_trans': hotel_name_trans,
        'min_total_price': min_total_price,
        'hotel_name': hotel_name,
        'main_photo_url': main_photo_url,
    }

    return render(request, 'index.html', context)

# Other view functions remain unchanged
=======

from item.models import Item 

from .forms import SignupForm, LoginForm

from django.contrib.sessions.models import Session



# Create your views here.
def home(request):
    items = Item.objects.filter(is_active=True)[0:6]

    return render(request,  'index.html', {
        'items': items,
        })

>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038

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
<<<<<<< HEAD
    })
=======
    })
>>>>>>> 4fdda5b4a658ec79584c478eb3ae25454cf1a038
