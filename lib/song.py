class Song:
    count = 0  # Class attribute to track the number of songs created
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to store count of songs per genre
    artist_count = {}  # Class attribute to store count of songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count whenever a new song is created
        Song.add_song_to_count()
        
        # Add the genre and artist to their respective lists and counts
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count whenever a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a new genre to the genres list, ensuring no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds a new artist to the artists list, ensuring no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Adds the genre to the genre_count dictionary and increments its count."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Adds the artist to the artist_count dictionary and increments its count."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

