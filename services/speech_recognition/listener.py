# Speech recognition service
# services/speech_recognition/listener.py - Speech recognition service

import speech_recognition as sr

def listen():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        # Listen for the first phrase and extract it into audio data
        audio = recognizer.listen(source)
        
    try:
        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except sr.UnknownValueError:
        # Speech was unintelligible
        print("I couldn't understand what was said.")
        return ""
    except sr.RequestError as e:
        # Could not request results from Google's speech recognition service
        print(f"Could not request results; {e}")
        return ""

# If you want to test the listener directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     print("Say something:")
#     text = listen()
