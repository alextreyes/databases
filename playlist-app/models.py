"""Models for Playlist app."""

  
from flask_sqlalchemy import SQLAlchemy

  

db = SQLAlchemy()

  
  

class Playlist(db.Model):
 """Playlist."""
 __tablename__ = 'playlists'
 id = db.Column(db.Integer,autoincrement=True,primary_key=True)
 name = db.Column(db.String(20),nullable=False)
 description = db.Column(db.Text,
                         nullable=False)
 songs = db.relationship("PlaylistSong", backref='playlist')

  
  

class Song(db.Model):
   """Song."""
   __tablename__ = 'songs'
   id = db.Column(db.Integer,
                  autoincrement=True,
                  primary_key=True)
   title = db.Column(db.String,
                     nullable=False)
   artist = db.Column(db.Text,
                      nullable=False)
   playlists = db.relationship("PlaylistSong", backref='song')

  
  

class PlaylistSong(db.Model):
   """Mapping of a playlist to a song."""
   __tablename__ = 'playlistsongs'
   id = db.Column(db.Integer,
                  autoincrement=True,
                  primary_key=True)
   playlist_id = db.Column(db.Integer,
                           db.ForeignKey('playlists.id'),
                           nullable=False)
   song_id = db.Column(db.Integer,
                       db.ForeignKey('songs.id'),
                       nullable=False)

  
  
  

# DO NOT MODIFY THIS FUNCTION

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

