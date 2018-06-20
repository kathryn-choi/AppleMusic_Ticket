from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

class Artist(models.Model):
    artistname = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'profile_image')
    info = models.TextField()
    genre = models.CharField(max_length=30)
    bio = models.TextField(default = '')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.artistname

def create_artist(sender, **kwargs):
    if kwargs['created'] :
        user_profile = Artist.object.create(user=kwargs['instance'])

post_save.connect(create_artist, sender=User)

class Concert(models.Model):
    artistname = models.ForeignKey(Artist, on_delete=models.CASCADE)
    venue = models.CharField(max_length=200 , blank = True)
    city = models.CharField(max_length=200, blank = True)
    region =  models.CharField(max_length=200, blank = True)
    country = models.CharField(max_length=200)
    published_date = models.DateTimeField(
        default=timezone.now)
    concert_date = models.DateField(
            null=True)
    ticketlink = models.URLField(default = '')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
