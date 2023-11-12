import openai
import os
import datetime

# Function to safely load API key from environment variable
# def load_api_key(env_var='OPENAI_API_KEY'):
#     api_key = os.getenv(env_var)
#     if api_key is None:
#         raise ValueError(f"The environment variable '{env_var}' is not set.")
#     return api_key


# Function to generate text using the fine-tuned model
def generate_text(prompt, model_id, max_tokens=500):
    try:
        # Load API key from environment variable for security
        openai.api_key = 'INSERT API KEY'

        # Generate text with the fine-tuned model
        response = openai.Completion.create(
            model=model_id,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=1
        )
        generated_text = response.choices[0].text.strip()
        usage = response.usage
        return generated_text, usage
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Function to calculate the cost of the request
def calculate_cost(usage):
    input_cost_per_token = 0.0016 / 1000  # Cost per token for input usage
    output_cost_per_token = 0.0016 / 1000  # Cost per token for output usage

    tokens_used = usage['total_tokens']
    cost = tokens_used * (input_cost_per_token + output_cost_per_token)
    return cost

# Main function to handle user input and display output
def main_generate_text():
    model_id = input("Enter your fine-tuned model ID: ").strip()
    prompt = input("Enter a prompt to generate text: ").strip()

    # Generate text
    generated_text, usage = generate_text(prompt, model_id)

    if generated_text:
        print("\nGenerated Text:\n", generated_text)
        if usage:
            cost = calculate_cost(usage)
            print(f"\nTokens used: {usage['total_tokens']}")
            print(f"Estimated cost of this request: ${cost:.6f}")

        # Define the output directory
        output_dir = "C:PATH"
        os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

        # Save to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_text_{timestamp}.txt"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Prompt: {prompt}\nCompletion: {generated_text}\n")
        print(f"Generated text saved to {file_path}")

    else:
        print("Failed to generate text.")


if __name__ == "__main__":
    main_generate_text()
