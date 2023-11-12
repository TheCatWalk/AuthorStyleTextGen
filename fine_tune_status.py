
import openai

openai.api_key = 'INSERT YOUR KEY'

# Replace 'your_fine_tune_id' with your actual fine-tune ID
fine_tune_id = 'INSERT FINE TUNE ID'

# Retrieve the fine-tuning job status
fine_tune_status = openai.FineTune.retrieve(id=fine_tune_id)
fine_tune_details = openai.FineTune.retrieve(id=fine_tune_id)

print(f"Fine-tuning status for ID {fine_tune_id}:")
print(f"Status: {fine_tune_status['status']}")
if fine_tune_status['status'] == 'succeeded':
    print("Your model is ready to use.")
elif fine_tune_status['status'] == 'failed':
    print("Fine-tuning failed. Check the error message for details.")
else:
    print("Fine-tuning is still in progress.")
print(fine_tune_details)

