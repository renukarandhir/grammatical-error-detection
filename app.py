from flask import Flask, request, render_template
import re

app = Flask(__name__)

error_labels = {
    'LABEL_0': 'No errors found.',
    'LABEL_1': 'Subject-verb agreement error.',
    'LABEL_2': 'Incorrect verb tense.',
    'LABEL_3': 'Punctuation error.',
    'LABEL_4': 'Missing article error.',
    'LABEL_5': 'Sentence fragment error.',
    'LABEL_6': 'Redundant word error.',
    'LABEL_7': 'Incorrect preposition usage.',
    'LABEL_8': 'Misplaced modifier error.',
    'LABEL_9': 'Unclear pronoun reference.',
    'LABEL_10': 'Improper name usage or identity error.',
}

def extract_name(sentence):
    """Extract potential name from the sentence."""
    # A very basic approach to extract a proper noun starting with a capital letter
    match = re.search(r'\bi was (\w+)\b', sentence, re.IGNORECASE)
    if match:
        return match.group(1)  # Extract the name
    return None

def check_grammar(sentence):
    sentence = sentence.strip()  # Normalize input
    if not sentence:
        return "LABEL_5"  # Sentence fragment if empty

    # Basic checks
    if sentence[-1] not in ['.', '!', '?']:
        return "LABEL_3"  # Punctuation error

    # Simulate more complex checks
    if "he go" in sentence or "they goes" in sentence:
        return "LABEL_1"  # Subject-verb agreement error
    elif "am going" in sentence and "yesterday" in sentence:
        return "LABEL_2"  # Incorrect verb tense
    elif "cat" in sentence and "a cat" not in sentence:
        return "LABEL_4"  # Missing article
    elif "very unique" in sentence:
        return "LABEL_6"  # Redundant word error
    elif "at" in sentence and "in" in sentence:
        return "LABEL_7"  # Incorrect preposition usage
    elif "only I saw" in sentence:
        return "LABEL_8"  # Misplaced modifier error
    elif "i was" in sentence and extract_name(sentence):
        return "LABEL_10"  # Improper name usage or identity error

    # More specific error checks
    if "the informations" in sentence:
        return "LABEL_1"  # Subject-verb agreement error (plural)
    elif "i seen" in sentence:
        return "LABEL_2"  # Incorrect verb tense
    elif "a apple" in sentence:
        return "LABEL_4"  # Missing article
    elif "absolutely essential" in sentence:
        return "LABEL_6"  # Redundant word error
    elif "I'm at home in the weekend." in sentence:
        return "LABEL_7"  # Incorrect preposition usage
    elif "She only eats cake on Sundays." in sentence:
        return "LABEL_8"  # Misplaced modifier error
    elif "He gave the book to John, who lent it to him." in sentence:
        return "LABEL_9"  # Unclear pronoun reference

    return "LABEL_0"  # Fallback: No errors found

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        sentence = request.form['sentence']
        output_label = check_grammar(sentence)  # Call the grammar checking function
        result = error_labels.get(output_label, 'Unknown error.')

        # Provide specific suggestions for corrections based on the output_label
        if output_label == 'LABEL_1':
            correction = "You should say 'He goes to school.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_2':
            correction = "Ensure correct verb tense usage. E.g., 'I went to school yesterday.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_3':
            correction = "Make sure your sentence ends with appropriate punctuation."
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_4':
            correction = "Consider adding an article before the noun. E.g., 'I see a cat.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_5':
            correction = "The sentence is a fragment. Please provide a complete sentence."
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_6':
            correction = "Avoid redundant phrases. E.g., 'unique' is sufficient."
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_7':
            correction = "Use the correct preposition. E.g., 'I will meet you at the cafe, tomorrow.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_8':
            correction = "Rephrase for clarity. E.g., 'She only eat cake on Sunday.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_9':
            correction = "Clarify the pronoun reference. E.g., 'She gave the book to Sarah.'"
            result += f" Suggested correction: {correction}"
        elif output_label == 'LABEL_10':
            name = extract_name(sentence)  # Extract the name from the sentence
            if name:
                correction = f"You should rephrase the sentence to 'I am {name}' or 'My name is {name}.'"
                result += f" Suggested correction: {correction}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)







#mkdir grammar-checker
#cd grammar-checker
#python -m venv venv
# `venv\Scripts\activate`
#pip install flask torch transformers nltk
#import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#ltk.download('wordnet')
