class ChatMemory:
    def __init__(self, window_size=3):
        self.window_size = window_size  # Number of conversation pairs
        self.history = []

    def add_exchange(self, user_input, bot_response):
        """Adds new conversation turn"""
        self.history.append(("User", user_input))
        self.history.append(("Bot", bot_response))
        
        # Remove oldest exchanges if over window limit
        while len(self.history) > self.window_size * 2:
            self.history = self.history[2:]  # Remove oldest pair

    def get_context(self):
        """Formats history as string for model input"""
        return "\n".join(
            [f"{role}: {text}" for role, text in self.history]
        )

# Test locally: python chat_memory.py
if __name__ == "__main__":
    memory = ChatMemory(window_size=2)
    memory.add_exchange("Hi", "Hello!")
    memory.add_exchange("How are you?", "I'm good!")
    print("Current context:")
    print(memory.get_context())