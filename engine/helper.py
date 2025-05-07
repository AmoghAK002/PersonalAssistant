import re
import string

# Extract YouTube search term
def extract_yt_term(command):
    pattern = r'play\s+(.+?)(?:\s+on\s+youtube)?$'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None 

# Remove unwanted words from input string
def remove_words(input_string, words_to_remove):
    # Remove punctuation for cleaner matching
    translator = str.maketrans('', '', string.punctuation)
    cleaned_input = input_string.translate(translator).lower().strip()

    # Split the cleaned input string into words
    words = cleaned_input.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string
