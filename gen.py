import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # This is for older Python versions that don't have the attribute
    pass
else:
    # Disables certificate verification
    ssl._create_default_https_context = _create_unverified_https_context

print("Attempting to download 'punkt'...")
try:
    nltk.download('punkt')
    print("'punkt' downloaded successfully!")
except Exception as e:
    print(f"An error occurred: {e}")