import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Download NLTK data files (only need to run once)
nltk.download('punkt')
nltk.download('stopwords')

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to process the command
def process_command(command):
    tokens = word_tokenize(command)
    filtered_words = [word for word in tokens if word.lower() not in stopwords.words('english')]
    
    if 'time' in filtered_words:
        #DEV.OMORI
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif 'name' in filtered_words:
        speak("My name is Voice Assistant.")
    else:
        speak("I am sorry, I can't understand the command.")

# Main function to capture and recognize speech
def main():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            process_command(command)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
