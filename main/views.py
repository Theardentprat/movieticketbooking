from django.shortcuts import render
from django.urls import reverse
from accounts.models import *
from random import choice
from .models import *
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'mov': movies,
        'movcoursel': movies[:5],
    }
    return render(request,"index.html", context)

def movies(request, id):
    #cin = Cinema.objects.filter(shows__movie=id).distinct()
    movies = Movie.objects.get(movie=id)
    cin = Cinema.objects.filter(cinema_show__movie=movies).prefetch_related('cinema_show').distinct()  # get all cinema
    show = Shows.objects.filter(movie=id)
    context = {
        'movies':movies,
        'show':show,
        'cin':cin,
    }
    return render(request, "movies.html", context )

def seat(request, id):
    show = Shows.objects.get(shows=id)
    seat = Bookings.objects.filter(shows=id)
    pks = Advertisement.objects.values_list('pk', flat=True)
    if pks.count() > 0:
        random_pk = choice(pks)
        random_obj = Advertisement.objects.get(pk=random_pk)
    return render(request,"seat.html", {'show':show, 'seat':seat, 'advert_url': random_obj.url if pks.count() > 0 else False, 'discount': request.session.get(id, 0)})  #type: ignore  

def booked(request):
    if request.method == 'POST':
        user = request.user
        seat = ','.join(request.POST.getlist('check'))
        show = request.POST['show']
        viewd_Ads = int(request.POST['discount'])
        request.session[show] = viewd_Ads
        
        if len(seat) == 0:
            messages.error(request, "Please select a seat")
            return redirect(request.META.get('HTTP_REFERER'))
        book = Bookings(useat=seat, shows_id=show, user=user, discount=True if bool(int(request.POST['discount'])) else False, price=len(request.POST.getlist('check'))*(Shows.objects.get(shows=show)).price)
        book.save()
        messages.success(request, "The booking has been confirmed!")
        return redirect(reverse('ticket', kwargs={'id': book.id}))   #type:ignore 
        

def ticket(request, id):
    ticket = Bookings.objects.get(id=id)
    return render(request,"ticket.html", {'ticket':ticket})
