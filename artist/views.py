from django.shortcuts import render, get_object_or_404
from .forms import ConcertForm
from artist.models import Artist, Concert
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
    concerts = Concert.objects.filter(artistname = artist).order_by('concert_date')
    g = GeoIP2('geoip')
    ip = get_client_ip(request)
    client_countyname = g.country_code(ip)
    client_region = g.region(ip)
    return render(request, 'artist/artist_page.html', {'artist' : artist, 'concerts' : concerts, 'client_ip': ip, 'client_region':client_region,'client_countyname':client_countyname})
