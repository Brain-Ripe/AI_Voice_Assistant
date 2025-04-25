import wikipedia

def handle_general_query(text):
    try:
        result = wikipedia.summary(text, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"That was a bit too vague. Did you mean: {e.options[0]}?"
    except wikipedia.exceptions.PageError:
        return "I couldn't find anything relevant on Wikipedia."
    except Exception:
        return "Something went wrong while searching Wikipedia."
