import openai
import os
import time

openai.api_key = 'API KEY'

# Function to upload a file and return the file ID
def upload_file(file_path):
    try:
        response = openai.File.create(file=open(file_path, 'rb'), purpose='fine-tune')
        file_id = response['id']
        print(f"File '{file_path}' uploaded successfully. File ID: {file_id}")
        return file_id
    except Exception as e:
        print(f"Failed to upload file '{file_path}'. Error: {e}")
        return None

# Function to print a simple text-based progress bar
def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

# Function to start the fine-tuning process
def start_fine_tuning(training_file_id, validation_file_id):
    try:
        print("Starting fine-tuning...")
        response = openai.FineTune.create(
            training_file=training_file_id,
            validation_file=validation_file_id,
            model='babbage',
            n_epochs=4,
            batch_size=4,
            learning_rate_multiplier=0.1
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define the paths to your training and validation files
training_file_path = 'C:PATH to JASONL FILE'
validation_file_path = 'C:PATH TO JASONL FILE'

# Check if the files exist before proceeding
if not os.path.isfile(training_file_path):
    raise FileNotFoundError(f"Training file not found: {training_file_path}")

if not os.path.isfile(validation_file_path):
    raise FileNotFoundError(f"Validation file not found: {validation_file_path}")

# Upload the training and validation files to OpenAI and get their IDs
training_file_id = upload_file(training_file_path)
validation_file_id = upload_file(validation_file_path)

if training_file_id is None or validation_file_id is None:
    print("Failed to upload files. Fine-tuning cannot proceed.")
else:
    # Start the fine-tuning process and print the response
    response = start_fine_tuning(training_file_id, validation_file_id)
    if response:
        print("Fine-tuning started successfully.")
        print("Fine-tune ID:", response["id"])
        # Simulate a loading bar (since we don't have real-time progress updates)
        for i in range(100):
            time.sleep(0.1)  # Sleep for a short time to simulate work
            print_progress_bar(i + 1, 100, prefix='Progress:', suffix='Complete', length=50)
    else:
        print("Failed to start fine-tuning.")

if __name__ == "__main__":
    pass  # Replace 'pass' with any code you want to run when this script is executed directly
