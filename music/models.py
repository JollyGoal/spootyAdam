from django.db import models


class Music(models.Model):
    name = models.CharField('Songs', max_length=100)
    favorite = models.BooleanField('Favorites')
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    spotify_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Download(models.Model):


class Track(models.Model):
    name = models.CharField("name", max_length=200, null=True, db_index=True)
    artists = models.CharField(max_length=200, null=True, db_index=True)
    spotify_id = models.CharField(max_length=200, null=True, unique=True)
    apple_music_id = models.CharField(max_length=200, null=True, unique=True)


class Register(models.Model):
    profile_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=50, null=True)
    gender = CONTENT_TYPES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    type = models.CharField("Gender", max_length=6, help_text="Are you male or female ? .",
                            choices=CONTENT_TYPES, default='M')
    date_of_birth = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class CurrentSong(models.Model):
    queue_key = models.IntegerField()
    manually_requested = models.BooleanField()
    votes = models.IntegerField()
    internal_url = models.CharField(max_length=2000)
    external_url = models.CharField(max_length=2000, blank=True)
    artist = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
