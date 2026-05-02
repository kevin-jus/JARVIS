# JARVIS

A keyword-driven voice assistant built with Python. JARVIS listens for spoken commands, matches them against a defined set of intents, and responds via text-to-speech — integrating Wikipedia, live weather data, and media playback.

> **Note:** This project is not an AI. JARVIS uses deterministic keyword matching — there is no machine learning, no language model, and no neural network. It is a single-file Python script built for learning and experimentation.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Application Flow](#application-flow)
- [Supported Commands](#supported-commands)
- [How It Works](#how-it-works)
  - [Speech Recognition](#speech-recognition)
  - [Text-to-Speech](#text-to-speech)
  - [Wikipedia Lookup](#wikipedia-lookup)
  - [Weather Forecast](#weather-forecast)
  - [Media Playback](#media-playback)
  - [Command Matching](#command-matching)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Capability | Details |
|---|---|
| Voice input | Captures microphone audio and transcribes it via the Google Speech Recognition API |
| Text-to-speech | Responds aloud using the system's built-in TTS engine (`pyttsx3`) |
| Wikipedia lookup | Returns a 4-sentence summary for any "what is / who is" query |
| Weather forecast | Reports live temperature and conditions for a named city via OpenWeatherMap |
| Media | Opens YouTube directly, or plays a randomly selected track from a curated URL list |
| Basic controls | Reports its own name, pauses on request, and exits cleanly |

---

## Tech Stack

| Technology | Details |
|---|---|
| Language | Python 3.x |
| Speech recognition | `SpeechRecognition` + Google Speech Recognition API |
| Text-to-speech | `pyttsx3` (system-native engine, no internet required) |
| Knowledge | `wikipedia` Python library |
| Weather | OpenWeatherMap REST API (`requests`) |
| Media | `os.system("start ...")` to open URLs in the default browser |

---

## Project Structure

```
JARVIS/
│
├── JARVIS.py      # Single-file application — all logic lives here
└── LICENSE        # MIT License
```

All functionality — speech capture, intent matching, Wikipedia queries, weather lookups, and media playback — is implemented in `JARVIS.py`.

---

## Getting Started

### Prerequisites

- Python 3.x
- A working microphone
- Internet connection (required for speech recognition, Wikipedia, and weather)
- Windows (URL launching uses the Windows-only `start` command)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/kevin-jus/JARVIS.git
    cd JARVIS
    ```

2. **Install dependencies**

    ```bash
    pip install speechrecognition wikipedia pyttsx3 requests
    ```

3. **Run the assistant**

    ```bash
    python JARVIS.py
    ```

### Configuration

JARVIS requires a free OpenWeatherMap API key for the weather feature.

1. Register at <https://openweathermap.org/api> and copy your key.
2. Open `JARVIS.py` and replace the placeholder value on this line:

    ```python
    api_key = 'YOUR_API_KEY_HERE'
    ```

> **Security note:** Never commit a real API key to a public repository. Consider loading it from an environment variable instead.

---

## Application Flow

```
 ┌─────────────────────────────────────────┐
 │             Application Start           │
 │   speak("Hi, I'm your AI assistant…")   │
 └───────────────────┬─────────────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  listen()       │  ← microphone input
            │  Capture audio  │
            │  Transcribe     │
            └────────┬────────┘
                     │ transcribed text (lowercase)
                     ▼
         ┌───────────────────────┐
         │   Keyword matching    │
         │  (if / elif chain)    │
         └──┬──────────┬─────┬───┘
            │          │     │
     ┌──────▼──┐  ┌────▼──┐  └──► ... (other intents)
     │Wikipedia│  │Weather│
     │ lookup  │  │  API  │
     └─────────┘  └───────┘
            │
            ▼
       speak(response)   ← TTS output
            │
            ▼
    loop back to listen()
         (or exit)
```

---

## Supported Commands

All matching is case-insensitive and substring-based. The transcribed speech is converted to lowercase before any comparison.

| Voice command | Action |
|---|---|
| `"what is [topic]"` / `"who is [person]"` | Fetches and reads a 4-sentence Wikipedia summary |
| `"weather forecast of [city]"` | Reads live temperature and weather description for the city |
| `"your name"` | Responds with the assistant's name |
| `"please wait"` | Announces a 10-second pause and sleeps |
| `"open youtube"` | Opens `www.youtube.com` in the default browser |
| `"play some music"` | Picks a random URL from the playlist and opens it |
| `"quit"` / `"exit"` | Speaks a goodbye message and terminates the loop |

Any unrecognised input returns: *"Sorry, I can't do that yet. Please try again."*

---

## How It Works

### Speech Recognition

JARVIS uses the `SpeechRecognition` library with a `Microphone` input source. Before capturing audio, `adjust_for_ambient_noise()` calibrates the recogniser to the current background noise level. The captured audio is then sent to Google's Speech Recognition API, which returns a transcribed string. The result is converted to lowercase before any matching is performed.

If the API cannot understand the audio, `UnknownValueError` is caught and an empty string is returned. If the API is unreachable, `RequestError` is caught and an appropriate message is printed.

### Text-to-Speech

`pyttsx3` initialises a TTS engine backed by the operating system's native speech synthesiser (SAPI5 on Windows). The `speak()` helper calls `engine.say(text)` followed by `engine.runAndWait()`, which blocks until the audio has finished playing. This ensures responses are delivered in sequence before the next `listen()` call begins.

### Wikipedia Lookup

When the transcribed text contains `"what is"` or `"who is"`, JARVIS strips those leading words and passes the remainder to `wikipedia.summary(query, sentences=4)`. The returned excerpt (up to 4 sentences) is both printed to the console and read aloud via `speak()`.

### Weather Forecast

When the phrase `"weather forecast of"` is detected, the city name is extracted by splitting on that substring. A GET request is made to the OpenWeatherMap `/data/2.5/weather` endpoint with `units=metric`. If the response code is `200`, temperature and description fields are extracted from the JSON payload and read aloud. A failed lookup (non-200 response) triggers an error message via TTS.

### Media Playback

- **`"open youtube"`** — passes `www.youtube.com` to `os.system("start ...")`, which opens the URL in the system's default browser.
- **`"play some music"`** — shuffles a hardcoded list of 4 YouTube URLs, then selects one with `random.choice()` and opens it the same way. After launching, the loop exits (`break`).

### Command Matching

The main loop is a straightforward `if / elif / else` chain. Each branch checks whether a keyword or phrase is a substring of the lowercased transcription. There is no intent classification, fuzzy matching, or natural-language understanding — if the expected phrase is not present in the transcribed text, the input falls through to the default `else` branch.

---

## Known Limitations

| Limitation | Detail |
|---|---|
| Windows only | `os.system("start ...")` is Windows-exclusive; macOS and Linux are not supported |
| No conversational context | Each command is independent; there is no memory between turns |
| Hardcoded playlist | The music list contains exactly 4 fixed YouTube URLs defined in the source |
| API key in source | The OpenWeatherMap key is stored as a plain string; do not commit a real key publicly |
| No wake word | The assistant is always listening; it does not wait for an activation phrase |
| Single language | Speech recognition is configured for `en-in` (English, India); other locales are not supported |

---

## Contributing

Issues and pull requests are welcome. This is a small personal project — please keep the scope of contributions proportional. Large feature additions may not be accepted, but bug fixes and improvements to existing functionality are appreciated.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
