from django.shortcuts import render
import googlemaps
# Create your views here.
from googlemaps.exceptions import ApiError

gmaps = googlemaps.Client(key='AIzaSyAbOkxUWUw9z54up8AiMSCMX7rO7-8hqv8')

def printHotels(searchString, next=''):
    try:
        places_result = gmaps.places(query=searchString, page_token=next)
    except ApiError as e:
        print(e)
        return ''
    else:
        return places_result['results']

def gapp(request):

    data_hotel = printHotels('отели в Москве')

    context = {
        'data': data_hotel
    }

    return render(request, 'hotel/gapp.html', context)
