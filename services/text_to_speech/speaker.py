# services/text_to_speech/speaker.py - Text-to-speech service

import pyttsx3

def speak(text, rate=150, volume=1.0, voice_type='female'):
    """
    Convert text to speech and play it to the user using the pyttsx3 library.
    
    Parameters:
        text (str): The text to be spoken.
        rate (int): Speech rate, the number of words per minute.
        volume (float): Volume, range from 0.0 to 1.0.
        voice_type (str): Type of voice ('male' or 'female').
    """
    print(f"S.A.P.H.I.R.E. says: {text}")
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        # Set voice type
        if voice_type == 'female':
            engine.setProperty('voice', voices[1].id)  # Assuming the second voice is female
        else:
            engine.setProperty('voice', voices[0].id)  # Assuming the first voice is male
        
        # Set rate
        engine.setProperty('rate', rate)
        
        # Set volume
        engine.setProperty('volume', volume)
        
        engine.say(text)
        engine.runAndWait()  # Blocks while processing all currently queued commands
    except Exception as e:
        print(f"Failed to convert text to speech: {e}")

# If you want to test the speaker functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     text_to_speak = "Hello, I am S.A.P.H.I.R.E., your intelligent digital assistant."
#     speak(text_to_speak, rate=120, volume=0.9, voice_type='female')
