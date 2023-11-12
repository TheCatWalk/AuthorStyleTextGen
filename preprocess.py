import os
import re
import nltk
from datetime import datetime

nltk.download('punkt')

def preprocess_text(text):
    # Split text into paragraphs
    paragraphs = text.split('\n\n')
    preprocessed_paragraphs = []

    for paragraph in paragraphs:
        # Tokenize paragraph into sentences
        sentences = nltk.sent_tokenize(paragraph)
        preprocessed_sentences = []

        for sentence in sentences:
            # Convert to lowercase
            sentence = sentence.lower()


            # # Handle specific contractions and made-up terms
            # contractions = {
            #     "aren't": "are not",
            #     "can't": "cannot",
            #     "couldn't": "could not",
            #     "didn't": "did not",
            #     "doesn't": "does not",
            #     "don't": "do not",
            #     "hadn't": "had not",
            #     "hasn't": "has not",
            #     "haven't": "have not",
            #     "he'd": "he would",
            #     "he'll": "he will",
            #     "he's": "he is",
            #     "i'd": "i would",
            #     "i'll": "i will",
            #     "i'm": "i am",
            #     "i've": "i have",
            #     "isn't": "is not",
            #     "it's": "it is",
            #     "let's": "let us",
            #     "mightn't": "might not",
            #     "mustn't": "must not",
            #     "shan't": "shall not",
            #     "she'd": "she would",
            #     "she'll": "she will",
            #     "she's": "she is",
            #     "shouldn't": "should not",
            #     "that's": "that is",
            #     "there's": "there is",
            #     "they'd": "they would",
            #     "they'll": "they will",
            #     "they're": "they are",
            #     "they've": "they have",
            #     "we'd": "we would",
            #     "we're": "we are",
            #     "weren't": "were not",
            #     "we've": "we have",
            #     "what'll": "what will",
            #     "what're": "what are",
            #     "what's": "what is",
            #     "what've": "what have",
            #     "where's": "where is",
            #     "who'd": "who would",
            #     "who'll": "who will",
            #     "who're": "who are",
            #     "who's": "who is",
            #     "who've": "who have",
            #     "won't": "will not",
            #     "wouldn't": "would not",
            #     "you'd": "you would",
            #     "you'll": "you will",
            #     "you're": "you are",
            #     "you've": "you have",
            #     "'re": " are",
            #     "wasn't": "was not",
            #     "we'll": " will",
            #     "tryin'": "trying"
            # }
            #
            # for contraction, expansion in contractions.items():
            #     sentence = sentence.replace(contraction, expansion)

            # Remove special characters while preserving sentence-ending punctuation

            sentence = re.sub(r"[^\w\s'.!?-]", '', sentence)

            # Replace multiple spaces with a single space
            sentence = re.sub(r'\s+', ' ', sentence).strip()

            preprocessed_sentences.append(sentence)

        preprocessed_paragraph = ' '.join(preprocessed_sentences)
        preprocessed_paragraphs.append(preprocessed_paragraph)

    return '\n\n'.join(preprocessed_paragraphs)

# Get current date and time for file naming
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

def save_preprocessed_text(text, output_folder, file_name=f"bfmt_{current_datetime}_preprocessed_text.txt"):
    # Create a new folder in the specified directory
    folder_path = os.path.join(output_folder, "bfmt_preprocessed")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save the preprocessed text to a file
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Preprocessed text saved to {file_path}")