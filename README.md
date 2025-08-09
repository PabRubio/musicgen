## Commands

### Setup Environment
```bash
# Activate virtual environment
source venv/bin/activate

# Install required dependencies (if not already installed)
pip install transformers torch soundfile numpy
```

### Generate Audio
```bash
# Run the main audio generation script
python3 app.py
```

### Run Web Interface
```bash
# Open index.html directly in browser or serve locally:
python3 -m http.server 8000
# Then navigate to http://localhost:8000
```

## Architecture

This is a **Mood-to-Music Generator** that creates ambient audio using Facebook's MusicGen AI model.

### Core Components

1. **app.py** - Main Python script that:
   - Uses Hugging Face's `transformers` library to load `facebook/musicgen-small` model
   - Generates 5-second ambient audio clips for each mood
   - Saves audio as WAV files in `static/` directory
   - Contains PROMPTS dictionary mapping moods to descriptive text

2. **index.html** - Standalone web interface that:
   - Provides interactive mood selection through floating bubbles
   - Plays pre-generated audio files using HTML5 Audio API
   - Works without any external dependencies or frameworks

3. **Audio Files** - Pre-generated WAV files in `static/`:
   - angry.wav, calm.wav, dreamy.wav, happy.wav, sad.wav

### Mood Prompt Mappings

The application generates audio for 5 moods using these text prompts:
- **Calm**: "calm ambient pads, soft piano, gentle reverb, relaxing, cinematic"
- **Sad**: "slow minor key, sparse piano and soft strings, melancholic, low tempo"
- **Happy**: "bright upbeat melody, acoustic guitar, handclaps, cheerful, pop feel"
- **Angry**: "aggressive distorted synths and heavy drums, intense, high energy"
- **Dreamy**: "airy pads, shimmering bells, ethereal, spacious reverb"

### Key Dependencies

- `transformers` - Hugging Face library for MusicGen model
- `torch` - PyTorch for ML operations
- `soundfile` - Audio file I/O
- `numpy` - Numerical operations

Note: The project uses a Python virtual environment (`venv/`) for dependency isolation.