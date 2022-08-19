from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):

    Language_Choice = (
              ('Hindi', 'Hindi'),
              ('English', 'English'),
          )

    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    language = models.CharField(max_length=20,choices=Language_Choice,default='Hindi')
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


#MusicTalk
class Blog(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    # 좋아요
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

#댓글
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 

    def __str__(self):
        return self.comment #comment을 보여줌