# JARVIS
Your daily dose of AI magic—think of it as your personal Siri or Google Assistant, but with a fun twist (and not an actual AI)!

## README

### JARVIS
JARVIS is an interactive AI voice assistant built with Python. It mimics the behavior of popular voice assistants like Google Assistant and Siri, providing a fun and engaging user experience.

### Features
- **Speech Recognition**: Understands and interprets spoken queries.
- **Wikipedia Integration**: Fetches and reads out information from Wikipedia.
- **Text-to-Speech**: Converts text responses to spoken words.
- **Weather Forecast**: Retrieves current weather information for specified cities.
- **Music Player**: Plays random songs from a list of YouTube URLs.
- **Simple Commands**: Responds to basic commands like introducing itself, waiting, and opening YouTube.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/kevin-jus/JARVIS.git
    cd JARVIS
    ```

2. Install the required libraries:
    ```bash
    pip install speechrecognition wikipedia pyttsx3 requests
    ```

3. Set up your OpenWeatherMap API key:
    Replace `'035da0fd91dd054789a8bfd2c95cdf60'` with your own OpenWeatherMap API key in the code.

### Usage
1. Run the script:
    ```bash
    python JARVIS.py
    ```

2. Interact with JARVIS:
    - Ask questions starting with "what is" or "who is" to get Wikipedia summaries.
    - Say "weather forecast of [city]" to get current weather information.
    - Use simple commands like "your name", "please wait", "open YouTube", "play some music", "quit", or "exit".

### Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
