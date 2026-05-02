# JARVIS

A small hobbyist voice assistant script written in Python. **This is not AI.** It listens for your voice, matches keywords, and responds with pre-defined actions — nothing more, nothing less. Think of it as a fun weekend project, not a product.

## What it actually does

- Listens to your microphone using Google's free Speech Recognition API
- Matches what you said against a handful of hardcoded keywords
- Speaks back using your system's text-to-speech engine (`pyttsx3`)
- Looks up a Wikipedia summary if you say "what is" or "who is"
- Fetches current weather from OpenWeatherMap if you say "weather forecast of [city]"
- Opens YouTube or plays a random song from a small hardcoded list of YouTube URLs
- Waits 10 seconds if you say "please wait"
- Exits if you say "quit" or "exit"

That's it. There's no machine learning, no large language model, no neural network. It's a single Python file with an `if/elif` chain.

## Requirements

- Python 3.x
- A working microphone
- Internet connection (for speech recognition, Wikipedia, and weather)

## Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/kevin-jus/JARVIS.git
    cd JARVIS
    ```

2. Install dependencies:
    ```bash
    pip install speechrecognition wikipedia pyttsx3 requests
    ```

3. Get a free OpenWeatherMap API key at https://openweathermap.org/api and replace the hardcoded key in `JARVIS.py`:
    ```python
    api_key = 'YOUR_API_KEY_HERE'
    ```

## Usage

```bash
python JARVIS.py
```

Speak one of the supported commands:

| What you say | What happens |
|---|---|
| "what is [topic]" / "who is [person]" | Reads a Wikipedia summary |
| "weather forecast of [city]" | Reads current weather |
| "your name" | It tells you its name |
| "please wait" | Waits 10 seconds |
| "open youtube" | Opens youtube.com in your browser |
| "play some music" | Opens a random YouTube music link |
| "quit" / "exit" | Stops the script |

Anything else gets: *"Sorry, I can't do that yet."*

## Known limitations

- Windows-only for opening URLs (`os.system("start ...")`)
- The API key for OpenWeatherMap is hardcoded — remember to replace it before sharing your code
- No context, no memory, no conversation — every command is independent
- Music is just a list of 4 hardcoded YouTube links

## License

MIT — see [LICENSE](LICENSE).
