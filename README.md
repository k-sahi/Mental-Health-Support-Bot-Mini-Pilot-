# Mental Health Support Bot (Pilot Project)

## 1. Project Goal & Ethical Vision

This project is a proof-of-concept for a simple, anonymous, and empathetic chatbot designed to support student mental health. Its primary goal is **not to act as a therapist**, but rather as a **compassionate signpost**. The bot listens to students, acknowledges their feelings, and guides them toward real-world, professional resources like university counseling services and crisis hotlines.

The project was built with a strong ethical framework:
- **Safety First:** The bot is hard-coded to recognize crisis keywords. If a crisis is detected, its immediate and only action is to provide the National Suicide & Crisis Lifeline number (988).
- **Privacy by Design:** The system does not ask for or store any Personally Identifiable Information (PII). Interaction logs are anonymized, only storing the detected *intent* and a session ID, not the user's raw text, to protect privacy while allowing for high-level analysis.
- **Scoped Responsibility:** The bot never gives advice, diagnoses, or attempts to solve a user's problems. Its scope is strictly limited to listening and providing resources.

## 2. The Core Problem Solved

Many students hesitate to seek mental health support due to stigma, uncertainty about where to go, or the intimidation of a first conversation. This chatbot aims to lower that barrier by providing:
- An **anonymous and non-judgmental** first point of contact.
- **Immediate access** to information about professional help.
- A **safe space** to articulate feelings without pressure.

## 3. How It Works: Architecture & Technology

This pilot project uses a simple but effective rule-based system.

- **Intent Detection:** The bot uses Python's `re` (regular expressions) library to scan user input for keywords and patterns associated with different emotional states (e.g., anxiety, depression, crisis).
- **Empathetic Responses:** Based on the detected intent, the bot provides a pre-written, empathetic response to validate the user's feelings.
- **Resource Redirection:** For non-crisis situations, the bot gently offers to provide contact information for university counseling services.
- **Data Logging for Improvement:** Anonymized interaction data (timestamp, session ID, detected intent) is stored in a local **SQLite** database. This data is invaluable for understanding common student concerns and identifying areas where the bot's recognition patterns need improvement.

### Technologies Used
- **Language:** Python 3
- **Core Logic:** NLTK (for tokenization), Regular Expressions (`re` module)
- **Database:** SQLite3 (for lightweight, local data logging)
- **Testing:** A comprehensive test suite (`bot_tester.py`) with over 150 labeled prompts to validate the bot's accuracy.

## 4. Getting Started

### Prerequisites
- Python 3.8 or newer.
- NLTK's 'punkt' package.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Mental_Health_Support_Bot
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You will need to create a `requirements.txt` file containing `nltk`)*

4.  **Download NLTK data:**
    Run this command in your terminal to start a Python interpreter, then enter the commands:
    ```python
    import nltk
    nltk.download('punkt')
    exit()
    ```
    *(If you encounter an SSL error on macOS, see [this guide](https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed)).*

## 5. How to Use the Project

There are two main scripts:

1.  **Run the Chatbot:**
    To interact with the bot live, run the main script.
    ```bash
    python mental_health_bot.py
    ```

2.  **Validate the Bot's Accuracy:**
    To test the bot against the pre-built dataset of 150+ prompts and get an accuracy report, run the tester script.
    ```bash
    python bot_tester.py
    ```

## 6. Future Development & Scaling

This rule-based pilot serves as a solid foundation. The next logical step would be to replace the regex-based intent detection with a modern NLP model.

- **Upgrade Path:** The `detect_intent` function could be swapped with a **Hugging Face Transformers** model (e.g., a zero-shot classification model like `facebook/bart-large-mnli`). This would allow the bot to understand semantic meaning beyond simple keywords, making it far more robust and natural. The labeled dataset in `bot_tester.py` is perfectly suited to fine-tune such a model.