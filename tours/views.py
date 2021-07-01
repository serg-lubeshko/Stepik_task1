from django.shortcuts import render

def main_view(request):
    return render(request, template_name='tours/index.html')

def departure_view(request, departure):
    return render(request, template_name='tours/departure.html')

def tour_view(request, id):
    return render(request, template_name='tours/tour.html')


