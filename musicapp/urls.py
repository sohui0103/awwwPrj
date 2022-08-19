from django.urls import path
from musicapp import views

# Add URLConf
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.logo, name='logo'),
    path('index/', views.index, name='index'),
    path('<int:song_id>/', views.detail, name='detail'),
    path('mymusic/', views.mymusic, name='mymusic'),
    path('playlist/', views.playlist, name='playlist'),
    path('playlist/<str:playlist_name>/', views.playlist_songs, name='playlist_songs'),
    path('favourite/', views.favourite, name='favourite'),
    path('all_songs/', views.all_songs, name='all_songs'),
    path('recent/', views.recent, name='recent'),
    path('hindi_songs/', views.hindi_songs, name='hindi_songs'),
    path('english_songs/', views.english_songs, name='english_songs'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('play_song/<int:song_id>/', views.play_song_index, name='play_song_index'),
    path('play_recent_song/<int:song_id>/', views.play_recent_song, name='play_recent_song'),

    #유저 플레이리스트
    path('userplaylist/', views.userplaylist, name='userplaylist'),

    #musictalk
    path('musictalk/', views.musictalk, name='musictalk'),
    path('detailmt/<int:blog_id>/', views.detailmt, name='detailmt'),
    path('create_comment/<int:blog_id>',
         views.create_comment, name='create_comment'),

    path('new_comment/<int:blog_id>', views.new_comment, name='new_comment'),     

    path('new/', views.new, name='new'),     
    path('create/', views.create, name='create'),
    #path('postcreate/', views.postcreate, name='postcreate'),
    #path('update/<int:blog_id>/', views.update, name='update'),
    #path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),

    # 삭제
    path('delete/<int:blog_id>', views.delete , name="delete"),

    # 수정
    path('detail/<int:blog_id>/edit', views.update, name="update"),

]
