import os
from datetime import datetime
from preprocess import preprocess_text, save_preprocessed_text
from format_data import format_data_for_openai_empty, format_data_for_openai_present, split_data, save_data_to_jsonl, \
    format_data_for_openai_empty_with_shuffle, format_data_for_openai_present_with_first


def main():
    # Define file paths
    input_folder = "C:\\PATH TO INPUT FOLDER"
    input_file_name = "filename.txt"
    input_file_path = os.path.join(input_folder, input_file_name)

    # Read text from file
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"The file {input_file_path} was not found.")
        text = ""

    # Check if text is not empty before processing
    if text:
        preprocessed_text = preprocess_text(text)
        save_preprocessed_text(preprocessed_text, input_folder)

        # Get current date and time for file naming
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Process for empty prompts
        examples_empty = format_data_for_openai_empty(preprocessed_text)
        train_data_empty, validation_data_empty = split_data(examples_empty)

        # Define output paths for empty prompts
        train_file_path_empty = os.path.join(input_folder, "empty", f"fmt_{current_datetime}_train_data_e.jsonl")
        validation_file_path_empty = os.path.join(input_folder, "empty", f"fmt_{current_datetime}_validation_data_e.jsonl")

        # Save the data for empty prompts
        save_data_to_jsonl(train_data_empty, train_file_path_empty)
        save_data_to_jsonl(validation_data_empty, validation_file_path_empty)

        # Process for empty prompts with shuffle
        examples_empty_shuffle = format_data_for_openai_empty_with_shuffle(preprocessed_text)
        train_data_empty_shuffle, validation_data_empty_shuffle = split_data(examples_empty_shuffle)

        # Define output paths for empty prompts with shuffle
        train_file_path_empty_shuffle = os.path.join(input_folder, "empty_shuffle", f"fmt_{current_datetime}_train_data_es.jsonl")
        validation_file_path_empty_shuffle = os.path.join(input_folder, "empty_shuffle", f"fmt_{current_datetime}_validation_data_es.jsonl")

        # Save the data for empty prompts with shuffle
        save_data_to_jsonl(train_data_empty_shuffle, train_file_path_empty_shuffle)
        save_data_to_jsonl(validation_data_empty_shuffle, validation_file_path_empty_shuffle)

        # Process for previous sentence prompts with first prompt empty
        examples_present = format_data_for_openai_present(preprocessed_text)
        train_data_present, validation_data_present = split_data(examples_present)

        # Define output paths for previous sentence prompts with first prompt empty
        train_file_path_present = os.path.join(input_folder, "present_fn", f"fmt_{current_datetime}_train_data_pfn.jsonl")
        validation_file_path_present = os.path.join(input_folder, "present_fn", f"fmt_{current_datetime}_validation_data_pfn.jsonl")

        # Save the data for previous sentence prompts with first prompt empty
        save_data_to_jsonl(train_data_present, train_file_path_present)
        save_data_to_jsonl(validation_data_present, validation_file_path_present)

        # Process for previous sentence prompts with first sentence given
        examples_present_first = format_data_for_openai_present_with_first(preprocessed_text)
        train_data_present_first, validation_data_present_first = split_data(examples_present_first)

        # Define output paths for previous sentence prompts with first sentence given
        train_file_path_present_first = os.path.join(input_folder, "present_fy", f"fmt_{current_datetime}_train_data_pfy.jsonl")
        validation_file_path_present_first = os.path.join(input_folder, "present_fy", f"fmt_{current_datetime}_validation_data_pfy.jsonl")

        # Save the data for previous sentence prompts with first sentence given
        save_data_to_jsonl(train_data_present_first, train_file_path_present_first)
        save_data_to_jsonl(validation_data_present_first, validation_file_path_present_first)

    else:
        print("No text to preprocess.")

if __name__ == "__main__":
    main()
