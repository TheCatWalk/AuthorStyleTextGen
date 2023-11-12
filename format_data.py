import json
import random
import nltk
import os

# Define the separator and stop sequence
SEPARATOR = "\ContinueWriting:"
STOP_SEQUENCE = "\n"

# Empty prompts without shuffle
def format_data_for_openai_empty(text):
    examples = []
    paragraphs = text.split('\n\n')

    for paragraph in paragraphs:
        sentences = nltk.sent_tokenize(paragraph)

        # Sentence-Level Examples
        for sentence in sentences:
            examples.append({"prompt": "", "completion": f" {sentence}{STOP_SEQUENCE}"})

        # Combined Sentences
        combined_sentences = ' '.join(sentences)
        if 2 <= len(sentences) <= 5:
            examples.append({"prompt": SEPARATOR, "completion": f" {combined_sentences}{STOP_SEQUENCE}"})

    return examples

# Empty prompts with shuffle
def format_data_for_openai_empty_with_shuffle(text):
    examples = format_data_for_openai_empty(text)
    random.shuffle(examples)  # Shuffle the examples
    return examples

# Previous sentence as prompt, with the first prompt empty
def format_data_for_openai_present(text):
    examples = []
    sentences = nltk.sent_tokenize(text)
    for i in range(len(sentences)):
        # Using the previous sentence as a prompt for the current sentence
        prompt = f"{sentences[i - 1]}{SEPARATOR}" if i > 0 else ""
        completion = f" {sentences[i]}{STOP_SEQUENCE}"
        examples.append({"prompt": prompt, "completion": completion})
    return examples

# Previous sentence as prompt, with the first sentence given
def format_data_for_openai_present_with_first(text):
    examples = []
    sentences = nltk.sent_tokenize(text)
    for i in range(len(sentences)):
        prompt = f"{sentences[i - 1]}{SEPARATOR}" if i > 0 else sentences[0]
        completion = f" {sentences[i]}{STOP_SEQUENCE}"
        examples.append({"prompt": prompt, "completion": completion})
    return examples

# Split data without shuffle
def split_data(examples, split_ratio=0.9):
    split_idx = int(split_ratio * len(examples))
    train_data = examples[:split_idx]
    validation_data = examples[split_idx:]
    return train_data, validation_data

def save_data_to_jsonl(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        for example in data:
            f.write(json.dumps(example) + '\n')
    print(f"Data saved to {file_path}")
