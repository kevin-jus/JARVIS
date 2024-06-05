import speech_recognition as sr
import wikipedia
import pyttsx3
import requests
import random
import time
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Function to recognize speech using Google Speech Recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to process your request at the moment.")
        return ""

# Main program loop
if __name__ == "__main__":
    speak("Hi, I'm your AI assistant. How can I help you today?")
    while True:
        query = listen()
        if "what is" in query or "who is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)
        elif "your name" in query:
            speak("My name is jarvis")
        elif "weather forecast of" in query:
            def get_weather(api_key, city):
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url)
                data = response.json()
                return data
            
            api_key = '035da0fd91dd054789a8bfd2c95cdf60'
            
            query = query
        
            if "weather forecast of" in query:
                city = query.split("weather forecast of ")[1]
                weather_data = get_weather(api_key, city)
                if weather_data['cod'] == 200:  # Check if response is successful
                    speak(f"Weather forecast for {city}:")
                    speak(f"Temperature: {weather_data['main']['temp']}°C")
                    speak(f"Description: {weather_data['weather'][0]['description']}")
                    print(f"Weather forecast for {city}:")
                    print(f"Temperature: {weather_data['main']['temp']}°C")
                    print(f"Description: {weather_data['weather'][0]['description']}")
                else:
                    speak("Failed to fetch weather data. Please check the city name.")
        elif "please wait" in query:
            speak("waiting 10 seconds")
            time.sleep(10)
        elif "open youtube" in query:
            url="www.youtube.com"
            speak("opening youtube")
            os.system(f"start {url}")
            break
        elif "play some music" in query:
            url2=[
                "https://youtu.be/jGflUbPQfW8?si=cpsfnlIhamZm2bI6",
                "https://youtu.be/pRfmrE0ToTo?si=aFUC_4ZxvxuNGZLT",
                "https://youtu.be/3Kxf2dHlDpQ?si=g3BwAGdhApXJiruT",
                "https://youtu.be/e-ORhEE9VVg?si=CJE5pQYQrrEhEa2m"
            ]
            
            random.shuffle(url2)
            chosen_url=random.choice(url2)
            speak("playing some music")
            os.system(f"start {chosen_url}")
            break
        elif "quit" in query or "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't do that yet. Please try again.")