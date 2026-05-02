# JARVIS

A lightweight, keyword-driven voice assistant built with Python as a personal hobby project.

> **Note:** This is not an AI. JARVIS uses rule-based keyword matching — there is no machine learning, no language model, and no neural network involved. It is a single-file Python script intended for learning and experimentation.

---

## Features

| Capability | Details |
|---|---|
| Voice input | Captures microphone audio via the Google Speech Recognition API |
| Text-to-speech | Responds using the system's built-in TTS engine (`pyttsx3`) |
| Wikipedia lookup | Returns a short summary for "what is / who is" queries |
| Weather | Reports current conditions for a named city via OpenWeatherMap |
| Media | Opens YouTube or plays a random track from a curated URL list |
| Basic commands | Name, wait, and exit controls |

---

## Requirements

- Python 3.x
- A working microphone
- Internet connection (required for speech recognition, Wikipedia, and weather)

---

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/kevin-jus/JARVIS.git
    cd JARVIS
    ```

2. **Install dependencies**

    ```bash
    pip install speechrecognition wikipedia pyttsx3 requests
    ```

3. **Configure your OpenWeatherMap API key**

    Register for a free key at <https://openweathermap.org/api>, then open `JARVIS.py` and replace the placeholder:

    ```python
    api_key = 'YOUR_API_KEY_HERE'
    ```

---

## Usage

```bash
python JARVIS.py
```

Speak any of the supported commands listed below. Recognition is case-insensitive and based on substring matching.

| Voice command | Response |
|---|---|
| `"what is [topic]"` / `"who is [person]"` | Reads a 4-sentence Wikipedia summary |
| `"weather forecast of [city]"` | Reports temperature and weather description |
| `"your name"` | States the assistant's name |
| `"please wait"` | Pauses execution for 10 seconds |
| `"open youtube"` | Opens `youtube.com` in the default browser |
| `"play some music"` | Opens a randomly selected YouTube link |
| `"quit"` / `"exit"` | Terminates the script |

Unrecognised input returns: *"Sorry, I can't do that yet."*

---

## Known Limitations

- **Windows only** — URL and browser launching uses `os.system("start ...")`, which does not work on macOS or Linux.
- **No conversational context** — each command is handled independently; there is no memory between turns.
- **Hardcoded music list** — the playlist consists of 4 fixed YouTube URLs defined directly in the source.
- **API key in source** — the OpenWeatherMap key is stored in plain text; avoid committing your personal key to a public repository.

---

## Contributing

Issues and pull requests are welcome. This is a small personal project, so please keep expectations proportional — large feature requests may not be accepted.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
