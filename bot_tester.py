# We need to import the functions from your original bot script
from mental_health_bot import detect_intent, INTENTS

# --- Labeled Prompts Dataset ---
# This dataset is structured for testing the current bot or training a future AI model.
PROMPTS_DATA = [
    # --- Anxiety Prompts ---
    {'text': 'I feel so anxious all the time', 'intent': 'anxiety'},
    {'text': "I'm really worried about my future", 'intent': 'anxiety'},
    {'text': 'I have a big presentation and I am nervous', 'intent': 'anxiety'},
    {'text': 'I keep stressing out over small things', 'intent': 'anxiety'},
    {'text': 'I think I am panicking', 'intent': 'anxiety'},
    {'text': 'My heart is racing and I feel scared', 'intent': 'anixety'},
    {'text': "I'm overwhelmed with my schoolwork", 'intent': 'anxiety'},
    {'text': 'The thought of social events makes me nervous', 'intent': 'anxiety'},
    {'text': 'I am constantly on edge', 'intent': 'anxiety'},
    {'text': 'I can\'t stop worrying', 'intent': 'anxiety'},
    {'text': 'I have a lot of stress in my life right now', 'intent': 'anxiety'},
    {'text': 'I am freaking out about my exams', 'intent': 'anxiety'},
    {'text': 'Feeling a lot of pressure lately', 'intent': 'anxiety'},
    {'text': 'My anxiety is through the roof', 'intent': 'anxiety'},
    {'text': 'I am scared of failing', 'intent': 'anxiety'},
    {'text': 'What if things go wrong?', 'intent': 'anxiety'},
    {'text': 'I have this sense of dread', 'intent': 'anxiety'},
    {'text': "I'm just so tense", 'intent': 'anxiety'},
    {'text': 'I worry too much', 'intent': 'anxiety'},
    {'text': 'My stomach is in knots', 'intent': 'anxiety'},
    {'text': 'I feel a lot of internal pressure', 'intent': 'anxiety'},
    {'text': 'I have a fear of missing out', 'intent': 'anxiety'},

    # --- Depression Prompts ---
    {'text': 'I feel so sad and empty', 'intent': 'depression'},
    {'text': "I'm feeling really down today", 'intent': 'depression'},
    {'text': 'I feel miserable and alone', 'intent': 'depression'},
    {'text': 'I have no motivation to do anything', 'intent': 'depression'},
    {'text': "I can't get out of bed", 'intent': 'depression'},
    {'text': 'I feel lonely even when I am with people', 'intent': 'depression'},
    {'text': "I'm not interested in my hobbies anymore", 'intent': 'depression'},
    {'text': 'Everything feels pointless', 'intent': 'depression'},
    {'text': 'I feel blue', 'intent': 'depression'},
    {'text': "I'm crying for no reason", 'intent': 'depression'},
    {'text': 'I just feel so empty inside', 'intent': 'depression'},
    {'text': 'I feel a deep sadness', 'intent': 'depression'},
    {'text': 'I feel isolated from everyone', 'intent': 'depression'},
    {'text': 'Life feels heavy', 'intent': 'depression'},
    {'text': 'I am in a dark place', 'intent': 'depression'},
    {'text': 'Nothing makes me happy anymore', 'intent': 'depression'},
    {'text': 'I feel so drained', 'intent': 'depression'},
    {'text': "I'm tired of feeling this way", 'intent': 'depression'},
    {'text': 'I just want to be alone', 'intent': 'depression'},
    {'text': 'Feeling very low', 'intent': 'depression'},
    {'text': 'My mood has been terrible', 'intent': 'depression'},

    # --- Seeking Help Prompts ---
    {'text': 'I need help', 'intent': 'seeking_help'},
    {'text': 'Can I talk to someone?', 'intent': 'seeking_help'},
    {'text': 'I think I need counseling', 'intent': 'seeking_help'},
    {'text': 'Where can I find a therapist?', 'intent': 'seeking_help'},
    {'text': 'I need some support right now', 'intent': 'seeking_help'},
    {'text': 'Can you give me some resources?', 'intent': 'seeking_help'},
    {'text': 'I want to find professional help', 'intent': 'seeking_help'},
    {'text': 'Is there a support group?', 'intent': 'seeking_help'},
    {'text': 'Tell me about counseling services', 'intent': 'seeking_help'},
    {'text': 'I need guidance', 'intent': 'seeking_help'},
    {'text': 'I need to speak with a professional', 'intent': 'seeking_help'},
    {'text': 'I am looking for support options', 'intent': 'seeking_help'},

    # --- Crisis Prompts (CRITICAL FOR SAFETY) ---
    {'text': 'I want to kill myself', 'intent': 'crisis'},
    {'text': 'I want to die', 'intent': 'crisis'},
    {'text': 'I am going to end it all', 'intent': 'crisis'},
    {'text': 'I feel completely hopeless', 'intent': 'crisis'},
    {'text': 'There is no reason to live', 'intent': 'crisis'},
    {'text': 'My life is not worth living', 'intent': 'crisis'},
    {'text': 'I am thinking about suicide', 'intent': 'crisis'},
    {'text': 'The world is better off without me', 'intent': 'crisis'},
    {'text': "I'm going to commit suicide", 'intent': 'crisis'},
    {'text': 'I just want to end the pain', 'intent': 'crisis'},
    {'text': 'I feel like there is no way out', 'intent': 'crisis'},
    {'text': 'Life has no meaning and I want to end it', 'intent': 'crisis'},
    {'text': 'I am making a plan to kill myself', 'intent': 'crisis'},

    # --- Greeting Prompts ---
    {'text': 'hello', 'intent': 'greeting'},
    {'text': 'hi', 'intent': 'greeting'},
    {'text': 'hey there', 'intent': 'greeting'},
    {'text': 'good morning', 'intent': 'greeting'},
    {'text': 'yo', 'intent': 'greeting'},
    {'text': 'hi bot', 'intent': 'greeting'},
    {'text': 'heya', 'intent': 'greeting'},
    {'text': 'is anyone there?', 'intent': 'greeting'},
    {'text': 'Hi!', 'intent': 'greeting'},

    # --- Goodbye Prompts ---
    {'text': 'bye', 'intent': 'goodbye'},
    {'text': 'goodbye', 'intent': 'goodbye'},
    {'text': 'see you later', 'intent': 'goodbye'},
    {'text': 'gotta go now', 'intent': 'goodbye'},
    {'text': 'ok bye', 'intent': 'goodbye'},
    {'text': 'see ya', 'intent': 'goodbye'},
    {'text': 'I have to leave', 'intent': 'goodbye'},
    {'text': 'that is all for now, bye', 'intent': 'goodbye'},

    # --- Neutral / Unknown Prompts (To test for false positives) ---
    {'text': 'what is your name?', 'intent': 'unknown'},
    {'text': 'how were you made?', 'intent': 'unknown'},
    {'text': 'what is the weather like?', 'intent': 'unknown'},
    {'text': "I'm feeling hungry", 'intent': 'unknown'},
    {'text': 'I need to do my homework', 'intent': 'unknown'},
    {'text': 'This is interesting', 'intent': 'unknown'},
    {'text': 'Tell me a joke', 'intent': 'unknown'},
    {'text': 'My favorite color is blue', 'intent': 'unknown'},
    {'text': 'I am a student', 'intent': 'unknown'},
    {'text': 'I feel tired from my workout', 'intent': 'unknown'},
    {'text': 'I am happy today', 'intent': 'unknown'},
    {'text': 'I am feeling great!', 'intent': 'unknown'},
    {'text': 'I love this university', 'intent': 'unknown'},
    {'text': 'The sky is blue', 'intent': 'unknown'},
    {'text': 'I need to buy groceries', 'intent': 'unknown'},
    {'text': 'My back hurts from sitting', 'intent': 'unknown'},
]


def test_the_bot():
    """
    Runs all prompts through the bot's intent detection and reports the accuracy.
    """
    total_prompts = len(PROMPTS_DATA)
    correct_predictions = 0

    print("--- Starting Bot Validation Test ---")

    # Track which intents are performing poorly
    errors_by_intent = {intent: {'misses': 0, 'false_positives': 0} for intent in list(INTENTS.keys()) + ['unknown']}

    for item in PROMPTS_DATA:
        prompt_text = item['text']
        correct_intent = item['intent']

        detected_intent = detect_intent(prompt_text)

        if detected_intent == correct_intent:
            correct_predictions += 1
        else:
            print(f"\n--- MISMATCH ---")
            print(f"  Prompt: '{prompt_text}'")
            print(f"  - Correct Intent:   '{correct_intent}'")
            print(f"  - Bot Detected:     '{detected_intent}'")

            # Log the error for the summary
            if correct_intent in errors_by_intent:
                errors_by_intent[correct_intent]['misses'] += 1
            if detected_intent in errors_by_intent:
                errors_by_intent[detected_intent]['false_positives'] += 1

    print("\n\n--- Test Summary ---")
    accuracy = (correct_predictions / total_prompts) * 100
    print(f"Overall Accuracy: {correct_predictions} / {total_prompts} = {accuracy:.2f}%")

    print("\n--- Error Analysis by Intent ---")
    print(f"{'Intent':<15} | {'Times Missed':<15} | {'False Positives':<15}")
    print("-" * 50)
    for intent, errors in errors_by_intent.items():
        print(f"{intent:<15} | {errors['misses']:<15} | {errors['false_positives']:<15}")

    print("\n--- Next Steps ---")
    print("Review the 'MISMATCH' reports above.")
    print("If the bot missed an intent, consider updating the regex patterns in 'INTENTS' in your main bot file.")
    print("For example, if it missed 'I feel blue' for depression, you could add '\\b(blue)\\b' to the depression patterns.")


if __name__ == '__main__':
    test_the_bot()