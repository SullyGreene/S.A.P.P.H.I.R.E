# Wikipedia querying
# services/knowledge_bases/wikipedia.py - Wikipedia querying service

import wikipedia

def search_wikipedia(query):
    """
    Searches Wikipedia for a query and returns a summary of the top result.
    
    Parameters:
        query (str): The search query.
    
    Returns:
        str: A summary of the top Wikipedia page result or an error message.
    """
    try:
        # Set the language for Wikipedia articles
        wikipedia.set_lang("en")
        
        # Perform a search and get the top article's title
        results = wikipedia.search(query)
        if not results:
            return "No results found for your query."
        
        # Get a summary of the top article
        summary = wikipedia.summary(results[0], sentences=3)
        
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query matches multiple entries: {e.options}"
    except wikipedia.exceptions.PageError:
        return "The page you requested does not exist."
    except Exception as e:
        return f"An error occurred while fetching information from Wikipedia: {e}"

# If you want to test the Wikipedia search functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     query = "Python programming language"
#     print(f"Searching Wikipedia for '{query}'...")
#     result = search_wikipedia(query)
#     print("Result:\n", result)
