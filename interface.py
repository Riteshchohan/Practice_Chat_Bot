from model_loader import load_model
from chat_memory import ChatMemory

def main():
    # Initialize components
    model = load_model()
    memory = ChatMemory(window_size=3)
    
    print("Chatbot activated! Type '/exit' to quit")
    
    while True:
        # Get user input
        user_input = input("User: ").strip()
        
        # Exit command
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break
        
        # Generate context for model
        context = memory.get_context()
        full_prompt = f"{context}\nUser: {user_input}\nBot:"
        
        # Generate response
        output = model(
            full_prompt,
            max_new_tokens=50,
            pad_token_id=50256  # GPT2 end-of-text token
        )
        
        # Extract bot response
        bot_response = output[0]['generated_text'].split("Bot:")[-1].strip()
        
        # Update memory and show response
        memory.add_exchange(user_input, bot_response)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()