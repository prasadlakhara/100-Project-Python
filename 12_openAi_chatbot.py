import openai

# Set up the OpenAI API key (replace with your actual API key)
openai.api_key = 'your-api-key-here'

# Function to generate a response from GPT-3/GPT-4
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4",  # You can use "gpt-3.5-turbo" or "gpt-4" depending on availability and your API plan
            prompt=prompt,
            max_tokens=150,  # Control the length of the response
            temperature=0.7,  # Control randomness (lower for more controlled responses)
            top_p=1,  # Top probability for nucleus sampling
            frequency_penalty=0,  # Avoid repetitive text
            presence_penalty=0.6,  # Encourage the model to talk about new topics
            stop=["\n", "You:", "Chatbot:"]  # Stops generation when it hits these sequences
        )
        # Return the generated response text
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Chat function to handle the conversation loop
def chat():
    print("Chatbot is ready! Type 'exit' to end the conversation.")
    conversation_history = ""  # Store conversation history

    while True:
        # User input
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Add user input to conversation history
        conversation_history += f"You: {user_input}\n"

        # Get AI response
        ai_response = generate_response(conversation_history)
        print(f"Chatbot: {ai_response}")

        # Add AI response to conversation history for context
        conversation_history += f"Chatbot: {ai_response}\n"

if __name__ == "__main__":
    chat()
