from django.contrib import admin
from musicapp.models import *

# Register your models here.

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Favourite)
admin.site.register(Recent)
admin.site.register(Comment)
admin.site.register(Blog)