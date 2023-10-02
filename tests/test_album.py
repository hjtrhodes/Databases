from lib.album import Album

'''Constructs with fields'''
def test_album_constructs():
    album = Album(1, 'The White Album', 1968, 1)
    assert album.id == 1
    assert album.title == 'The White Album'
    assert album.release_year == 1968
    assert album.artist_id == 1


'''Construct with equality'''

'''Constructs so it looks pretty'''