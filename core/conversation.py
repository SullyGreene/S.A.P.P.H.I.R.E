# Conversation management
# core/conversation.py - Conversation management

from utils.helpers import open_website

# Import additional NLP functionalities
from services.natural_language_processing.nlp import (
    analyze_sentiment,
    detect_language,
    extract_entities,
    summarize_text
)

def handle_conversation(command):
    """
    Processes the user's command and returns an appropriate response.
    """
    responses = {
        "hello": "Hello! I'm Saphire, your assistant. How can I help you today?",
        "how are you": "I'm doing great, thank you! How can I assist you?",
        "what can you do": "I can perform tasks such as managing your calendar, sending emails, answering questions, opening websites, and more. What do you need help with?",
        "goodbye": "Goodbye! Have a great day!"
    }

    # Normalize the command to lowercase to simplify matching
    command_lower = command.lower()

    if command.startswith("take a note"):
        content = command.replace("take a note", "").strip()
        return bot_instance.note_service.add_note(content)
    elif command == "list my notes":
        return bot_instance.note_service.list_notes()
    elif command.startswith("find notes about"):
        query = command.replace("find notes about", "").strip()
        return bot_instance.note_service.find_notes(query)

    # New: Language Detection
    if "what language is this" in command_lower:
        # Assuming the actual text to analyze comes after this phrase in the command
        text_to_analyze = command_lower.split("this", 1)[1] if "this" in command_lower else None
        if text_to_analyze:
            language_code = detect_language(text_to_analyze)
            # Map the language code to a language name (simplified example)
            languages = {"en": "English", "fr": "French", "es": "Spanish"}
            language_name = languages.get(language_code, "an unknown language")
            return f"The text is in {language_name}."
        else:
            return "Please provide the text for language detection."

    # New: Sentiment Analysis
    if "analyze the sentiment of" in command_lower:
        text_to_analyze = command_lower.split("of", 1)[1] if "of" in command_lower else None
        if text_to_analyze:
            sentiment = analyze_sentiment(text_to_analyze)
            return f"The sentiment of the text is {sentiment}."
        else:
            return "Please provide the text for sentiment analysis."

    # New: Named Entity Recognition (Simplified example)
    if "what entities are in" in command_lower:
        text_to_analyze = command_lower.split("in", 1)[1] if "in" in command_lower else None
        if text_to_analyze:
            # For this example, assume `extract_entities` returns a string summary of entities
            entities = extract_entities(text_to_analyze)
            return f"The entities in the text are: {entities}"
        else:
            return "Please provide the text for entity extraction."

    # Existing website opening and default response handling remains unchanged

    # Check if the command matches any predefined responses
    if command_lower in responses:
        return responses[command_lower]

    # Additional command handling for more dynamic responses
    
    # Handle commands for opening websites
    if "open" in command_lower:
        website = command_lower.split("open ", 1)[1] if "open " in command_lower else None
        if website:
            if "youtube" in website:
                open_website("https://www.youtube.com")
                return "Opening YouTube."
            # Add additional website handling here
            else:
                # This is a placeholder for a more sophisticated website opening mechanism
                # For unknown websites, you could attempt to guess the URL or search for it
                return "I'm sorry, I can't open that website."
        else:
            return "Please tell me which website you'd like to open."

    # This response is returned if the command doesn't match any known commands or patterns
    return "I'm sorry, I didn't understand that. Can you try rephrasing?"
