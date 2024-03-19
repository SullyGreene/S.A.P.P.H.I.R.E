# Wolfram Alpha querying
# services/knowledge_bases/wolframalpha.py - Wolfram Alpha querying service

import wolframalpha

def query_wolframalpha(app_id, query):
    """
    Sends a query to Wolfram Alpha and returns the result.
    
    Parameters:
        app_id (str): The App ID for the Wolfram Alpha API.
        query (str): The search query.
    
    Returns:
        str: The first result from Wolfram Alpha or an error message.
    """
    try:
        # Initialize the Wolfram Alpha client with your App ID
        client = wolframalpha.Client(app_id)
        
        # Send the query to Wolfram Alpha
        res = client.query(query)
        
        # Attempt to extract and return the first result
        result = next(res.results).text
        return result
    except StopIteration:
        return "No results found."
    except Exception as e:
        return f"An error occurred while querying Wolfram Alpha: {e}"

# If you want to test the Wolfram Alpha querying functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     app_id = "YOUR_APP_ID_HERE"  # Replace with your Wolfram Alpha App ID
#     query = "distance from Earth to Moon"
#     print(f"Querying Wolfram Alpha for '{query}'...")
#     result = query_wolframalpha(app_id, query)
#     print("Result:\n", result)
