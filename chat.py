import ollama

# Define the model you want to use (e.g., 'mistral', 'gemma', or another Ollama-compatible model)
model = 'nigel'  # Change to another model if needed


running = True
while running:
    # Get user input
    user_input = input("You: ")

    # Run Ollama and get a response
    response = ollama.chat(model=model, messages=[
        {"role": "user", "content": user_input}
    ])

    # Print response
    print(response['message']['content'])

    # Check if the conversation should continue
    if response['message']['content'] == "Goodbye!" or user_input == "bye":
        running = False
