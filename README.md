# 🎵 **MCP PLAYLIST SERVER**

A Model Context Protocol (MCP) server that provides intelligent playlist curation tools using Spotify track data and audio feature analysis. This server enables AI assistants to create mood-based playlists, find similar songs, analyze audio characteristics, and curate personalized music collections.

## 🚀 **Features**

### Core MCP Tools

- **`create_mood_playlist`**: Generate playlists based on emotional states (happy, sad, energetic, calm, party, chill)
- **`find_similar_songs`**: Discover songs with similar audio characteristics using cosine similarity analysis
- **`analyze_song`**: Get comprehensive audio feature breakdown for any track
- **`create_genre_playlist`**: Build genre-focused playlists with customizable diversity levels
- **`get_dataset_stats`**: View detailed dataset statistics and insights

### Advanced Audio Analysis

The server analyzes multiple sophisticated audio characteristics:
- **Energy**: Track intensity and power measurement
- **Valence**: Musical positivity spectrum (happiness to sadness)
- **Danceability**: Rhythmic suitability for dancing
- **Acousticness**: Acoustic vs electronic instrumentation balance
- **Tempo**: Beats per minute analysis
- **Speechiness**: Spoken word content detection
- **Instrumentalness**: Vocal vs instrumental content ratio
- **Liveness**: Live performance detection
- **Popularity**: Track mainstream appeal metrics

## 🏗️ **Architecture**

```bash
├── server/
│   ├── main.py          # FastMCP server implementation
│   └── engine.py        # Playlist curation engine with ML algorithms
├── spotify_songs.csv  # Spotify dataset (32K+ songs)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 📋 **Requirements**

- **Python**: 3.10 or higher
- **Dataset**: Spotify tracks CSV with audio features
- **Dependencies**: Listed in `requirements.txt`

### Core Dependencies
- `fastmcp>=1.2.0` - Modern MCP server framework
- `pandas>=2.0.0` - Data manipulation and analysis
- `numpy>=1.24.0` - Numerical computing
- `scikit-learn>=1.3.0` - Machine learning algorithms

## 🛠️ **Installation**

### 1. Clone Repository
```bash
git clone https://github.com/alee2602/MCP-SERVER
```

### 2. Environment Setup

```bash
# Using Anaconda (recommended)
conda create -n mcp-playlist python=3.11
conda activate mcp-playlist

# Or using venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🧪 **Run the server**

```bash
python server/main.py
```

## 🔧 **Usage with MCP Hosts**

Claude Desktop Integration

1. Add to your **`claude_desktop_config.json`**:

```json
{
  "mcpServers": {
    "mcp-playlist": {
      "command": "python",
      "args": ["server/main.py"],
      "cwd": "/absolute/path/to/your/project"
    }
  }
}
```

2. Restart Claude Desktop
<br>

3. Use natural language commands
- "Create a chill playlist with 10 songs"
- "Find songs similar to Worldwide by Big Time Rush"
- "Analyze the audio features of Bohemian Rhapsody"

## Other MCP Clients
Configure with:

- **Protocol:** STDIO
- **Command:** python server/main.py
- **Working Directory:** Project root

## 📊 **API Examples**

1. Create a mood-based playlist

```json
{
  "method": "tools/call",
  "params": {
    "name": "create_mood_playlist",
    "arguments": {
      "mood": "energetic",
      "size": 15,
      "genre": "rock",
      "min_popularity": 50,
      "duration_minutes": 30
    }
  }
}
```

2. Create Genre Playlist
```json
{
  "method": "tools/call",
  "params": {
    "name": "create_genre_playlist",
    "arguments": {
      "genres": ["pop", "edm"],
      "size": 20,
      "diversity": "high"
    }
  }
}
```

3. Find similar songs
```json
{
  "method": "tools/call",
  "params": {
    "name": "find_similar_songs",
    "arguments": {
      "song_name": "Blinding Lights",
      "artist": "The Weeknd",
      "count": 8
    }
  }
}
```

4. Comprehensive Song Analysis
```json
{
  "method": "tools/call",
  "params": {
    "name": "analyze_song",
    "arguments": {
      "song_name": "Hotel California",
      "artist": "Eagles"
    }
  }
}
```
5. Get Dataset Statistics
```json
{
  "method": "tools/call",
  "params": {
    "name": "get_dataset_stats",
    "arguments": {}
  }
}
```

## 🔍 **Troubleshooting**

**1. "Dataset empty" Error**
- Verify **`spotify_songs.csv`** exists in project root
- Check file permissions and format
- Ensure required columns are present

**2. "Import Error" Messages**
```bash
pip install --upgrade fastmcp pandas scikit-learn
```
**Debug mode**
```bash
# Enable verbose logging
python server/main.py --debug
```
## 🙏 **Acknowledgments**

- [Anthropic MCP Protocol](https://modelcontextprotocol.io/) - Protocol specification
- [FastMCP Framework](https://gofastmcp.com/) - Python MCP implementation
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) - Audio feature reference
- [Kaggle Dataset](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs/data) - 30,000 Spotify Songs dataset by JoeBeachCapital
