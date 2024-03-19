# Core bot functionality
# core/bot.py - Core bot functionality
from core.conversation import handle_conversation
from services.speech_recognition.listener import listen
from services.text_to_speech.speaker import speak
from services.knowledge_bases.wikipedia import search_wikipedia
from services.knowledge_bases.wolframalpha import query_wolframalpha
from services.notations.taking_notes import NoteTakingService
from utils.logger import log
from config.settings import WOLFRAM_ALPHA_APP_ID

class SAPPHIREBot:
    def __init__(self):
        global bot_instance
        bot_instance = self
        self.note_service = NoteTakingService()
        log("S.A.P.P.H.I.R.E. initializing...")

    def start(self):
        log("S.A.P.P.H.I.R.E. is now running. Say 'quit' to stop.")
        speak("Hello, I am Sapphire., your intelligent digital assistant. How can I assist you today?")

        try:
            while True:
                user_input = listen()
                if user_input.lower() in ["quit", "exit", "goodbye"]:
                    speak("Goodbye!")
                    log("S.A.P.P.H.I.R.E. shutting down.")
                    break
                
                log(f"User said: {user_input}")
                response = self.process_input(user_input)
                speak(response)
        except Exception as e:
            log(f"An error occurred: {e}", level="ERROR")
            speak("I'm sorry, something went wrong.")

    def process_input(self, input_text):
        """
        Process the user's input and determine the appropriate response.
        """
        # Handling direct NLP functionality as an example
        if "analyze this text" in input_text.lower():
            # Assume `analyze_text` is a hypothetical direct NLP function you've implemented
            analysis_result = self.analyze_text(input_text)
            return analysis_result
    
        # Example of routing a query to Wikipedia
        if "wikipedia" in input_text.lower():
            query = input_text.replace("wikipedia", "")
            log(f"Searching Wikipedia for: {query}")
            return search_wikipedia(query)
        
        # Example of routing a query to Wolfram Alpha
        elif "calculate" in input_text.lower() or "what is" in input_text.lower():
            query = input_text.replace("calculate", "").replace("what is", "")
            log(f"Querying Wolfram Alpha for: {query}")
            return query_wolframalpha(WOLFRAM_ALPHA_APP_ID, query)
        
        # Fallback to simple conversation handling
        else:
            return handle_conversation(input_text)

# If you want to test the bot functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     bot = SAPHIREBot()
#     bot.start()
