import random
import re
import sqlite3
import datetime

# --- Intent Definitions ---
# We use regular expressions for more flexible keyword matching.
# The bot will check intents in this order. CRISIS must be first.
INTENTS = {
    'crisis': {
        'patterns': [r'.*\b(suicide|kill myself|want to die|hopeless|end it all)\b.*'],
        'responses': [
            "I'm truly sorry you're feeling this way. It's incredibly important that you talk to someone who can help right now. Please reach out immediately. You can call or text 988 in the US and Canada to connect with the Suicide & Crisis Lifeline. They are available 24/7, free, and confidential. Please, make the call."
        ]
    },
    'anxiety': {
        'patterns': [r'.*\b(anxious|worried|nervous|stressed|panicking)\b.*'],
        'responses': [
            "It sounds like you're dealing with a lot of stress right now. That can be really overwhelming.",
            "Feeling anxious is tough. Acknowledging it is a brave first step."
        ]
    },
    'depression': {
        'patterns': [r'.*\b(sad|depressed|empty|lonely|miserable)\b.*'],
        'responses': [
            "I'm sorry to hear you're feeling so down. It takes a lot of strength to even talk about it.",
            "It sounds like a heavy weight to carry. Please know that these feelings don't have to be permanent."
        ]
    },
    'seeking_help': {
        'patterns': [r'.*\b(help|talk to someone|counseling|therapist|support)\b.*'],
        'responses': ["It's a great step to be looking for support. Reaching out is a sign of strength."]
    },
    'greeting': {
        'patterns': [r'^\b(hello|hi|hey|yo)\b.*'],
        'responses': ["Hello! I'm here to listen and can help point you to some resources. How are you feeling today?"]
    },
    'goodbye': {
        'patterns': [r'.*\b(bye|goodbye|see you)\b.*'],
        'responses': ["Take care of yourself. Remember, help is available if you need it."]
    }
}

# --- Resource Information ---
RESOURCES = {
    "counseling_services": "Our university's Counseling and Psychological Services (CAPS) offers confidential support. You can find them at [Link to University Counseling Website] or call them at [Counseling Phone Number].",
    "online_articles": "Sometimes reading about what you're feeling can help. Mind.org.uk and NAMI.org have great, reliable articles.",
    "general_prompt": "Would you like me to share some resources, like contact info for university counseling or some helpful online articles?"
}


def detect_intent(user_message):
    """Detects the user's intent based on predefined patterns."""
    user_message = user_message.lower()
    for intent, data in INTENTS.items():
        for pattern in data['patterns']:
            if re.search(pattern, user_message):
                return intent
    return 'unknown'


def get_bot_response(intent):
    """Generates a bot response based on the detected intent."""
    if intent in INTENTS:
        # Get a standard response for the feeling
        primary_response = random.choice(INTENTS[intent]['responses'])

        # For non-crisis, non-greeting intents, add a prompt for resources
        if intent not in ['crisis', 'greeting', 'goodbye']:
            primary_response += " " + RESOURCES['general_prompt']

        return primary_response
    else:  # Unknown intent
        return "I'm not sure I understand, but I'm here to listen. " + RESOURCES['general_prompt']


def main_chat_loop():
    """The main loop to run the chatbot."""
    session_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # Simple unique session ID
    db_conn = setup_database()

    print("------------------------------------------------------------------")
    print("Mental Health Support Bot (Pilot)")
    print("Type 'bye' to exit. If you are in crisis, please say so.")
    print("Disclaimer: I am an automated bot, not a therapist. My purpose is to provide resources.")
    print("------------------------------------------------------------------\n")

    print("Bot: " + get_bot_response('greeting'))

    while True:
        user_input = input("You: ")

        intent = detect_intent(user_input)
        bot_response = get_bot_response(intent)

        print(f"Bot: {bot_response}")

        # Log the interaction (privacy-conscious)
        log_interaction(db_conn, session_id, intent, bot_response)

        # Special handling for crisis and help-seeking
        if intent == 'crisis':
            # In a real app, you might have extra logic here. For now, we exit to be safe.
            print("\nBot: Exiting to ensure you can focus on getting help. Please reach out now.")
            break

        if 'counseling' in user_input.lower() or 'resources' in user_input.lower():
            print(
                f"Bot: Of course. Here is the information for our counseling services: {RESOURCES['counseling_services']}")

        if intent == 'goodbye':
            break

    db_conn.close()


# --- Phase 2: Database Integration ---

def setup_database():
    """Creates an SQLite database and the interactions table if they don't exist."""
    conn = sqlite3.connect('interaction_logs.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS interactions
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       session_id
                       TEXT
                       NOT
                       NULL,
                       timestamp
                       DATETIME
                       NOT
                       NULL,
                       detected_intent
                       TEXT
                       NOT
                       NULL,
                       bot_response
                       TEXT
                       NOT
                       NULL
                   )
                   ''')
    conn.commit()
    return conn


def log_interaction(conn, session_id, intent, bot_response):
    """Logs the details of a single user-bot interaction."""
    cursor = conn.cursor()
    timestamp = datetime.datetime.now()
    cursor.execute('''
                   INSERT INTO interactions (session_id, timestamp, detected_intent, bot_response)
                   VALUES (?, ?, ?, ?)
                   ''', (session_id, timestamp, intent, bot_response))
    conn.commit()


if __name__ == '__main__':
    main_chat_loop()