from skills.system_controls import handle_system_commands
from skills.general_queries import handle_general_query

def handle_intent(text):
    text = text.lower()

    if any(x in text for x in ["open", "volume", "shutdown"]):
        return handle_system_commands(text)

    else:
        return handle_general_query(text)
