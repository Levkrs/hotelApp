from django.urls import path

import hotel.views

app_name = 'hotel'


urlpatterns = [
    path('', hotel.views.gapp, name='G hotel')
]