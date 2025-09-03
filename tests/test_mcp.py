import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

from server.engine import PlaylistEngine

def test_engine_functions():
    print("Testing playlist engine functions...")
    
    # Initialize engine
    engine = PlaylistEngine("spotify_songs.csv")
    
    # Test mood playlist
    print("\n1. Testing create_mood_playlist:")
    playlist = engine.create_mood_playlist(mood="sad", size=10)
    print(f"Sad playlist: {len(playlist)} songs")
    for i, song in enumerate(playlist, 1):
        print(f"  {i}. {song['name']} by {song['artists']}")
    
    # Test dataset stats
    print("\n2. Testing get_dataset_stats:")
    stats = engine.get_dataset_statistics()
    print(f"Total songs: {stats['total_songs']:,}")
    print(f"Unique artists: {stats['unique_artists']:,}")
    
    # Test similar songs
    print("\n3. Testing find_similar_songs:")
    sample_song = "Worldwide" 
    similar = engine.find_similar_songs(sample_song, count=3)
    if similar:
        print(f"Songs similar to '{sample_song}':")
        for song, similarity in similar:
            print(f"  - {song['track_name']} (similarity: {similarity:.3f})")
    else:
        print(f"No similar songs found for '{sample_song}'")

if __name__ == "__main__":
    test_engine_functions()