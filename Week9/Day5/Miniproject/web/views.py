from django.shortcuts import render



def home(request):
    return render(request, 'web/home.html')



from web.models import Hotel, Reservation


def hotel(request):
    hotels = Hotel.objects.order_by('-disponible')
    resers = Reservation.objects.all()
    return render(request, 'web/hotel.html', {"hotels":hotels, "resers":resers})
    
# Create your views here.
