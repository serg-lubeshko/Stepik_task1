from django.urls import path

from tours.views import main_view, departure_view, tour_view

urlpatterns = [
    path('', main_view, name='main'),
    path('departure/<str:departure>/', departure_view, name='departure'),
    path('tour/<int:pk>/', tour_view, name='tour'),
]
