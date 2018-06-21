from django.contrib import admin
from artist.models import Concert, Artist,Song

class ConcertAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'artistname', 'venue', 'city',
        'country', 'concert_date',)
    list_editable = ('concert_date', )
    list_filter = ('artistname', )

admin.site.register(Concert,ConcertAdmin)
admin.site.register(Artist)
admin.site.register(Song)
