from collections import defaultdict

def solution(genres, plays):
    genre_map = defaultdict(int)     
    song_map = defaultdict(list)

    for index, (genre, play_count) in enumerate(zip(genres, plays)):
        genre_map[genre] += play_count
        song_map[genre].append((index, play_count))

    sorted_genres = sorted(genre_map.keys(), key=lambda g: genre_map[g], reverse=True)
    
    best_album = []

    for genre in sorted_genres:
        songs = sorted(song_map[genre], key=lambda x: (-x[1], x[0]))
        best_album.extend([song[0] for song in songs[:2]])

    return best_album