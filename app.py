from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)


# Write a small program in app.py using the class AlbumRepository to print out the list of albums to the terminal.
album_repository = AlbumRepository(connection)
albums = album_repository.all()

for album in albums:
    print(album)