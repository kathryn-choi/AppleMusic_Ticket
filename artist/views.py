from django.shortcuts import render, get_object_or_404
from .forms import ConcertForm
from artist.models import Artist, Concert,Song
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.gis.geoip2 import GeoIP2

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def artist_list(request):
    artists = Artist.objects.order_by('artistname')
    return render(request, 'artist/artist_list.html', {'artists':artists})

def artist_page(request,pk):
    artist = get_object_or_404(Artist, pk=pk)
    songs = Song.objects.filter(artistname = artist.artistname).order_by('releasedate')
    recentsong = songs.first()
    concerts = Concert.objects.filter(artistname = artist).order_by('concert_date')
    g = GeoIP2('geoip')
    # New Zealand '121.72.165.118' '110.33.122.75'
    #cip = get_client_ip(request)
    cip = '110.33.122.75'
    client_country = g.country_name(cip)
    nearconcert = concerts.filter(country = client_country).order_by('concert_date')
    return render(request, 'artist/artist_page.html', {'artist' : artist, 'concerts' : concerts,
                'client_ip':cip,'client_country':client_country, 'nearconcert' : nearconcert, 'songs': songs,'recentsong': recentsong})
