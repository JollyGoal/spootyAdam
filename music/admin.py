from django.contrib import admin
from django import forms
from .models import Track, Register, Playlist, CurrentSong

admin.site.register(CurrentSong)
admin.site.register(Playlist)
admin.site.register(Register)
admin.site.register(Track)
