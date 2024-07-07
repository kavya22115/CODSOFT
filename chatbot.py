import re
class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': re.compile(r'\b(hello|hi|hey|greetings)\b', re.IGNORECASE),
            'name': re.compile(r'\b(name|who are you|your name)\b', re.IGNORECASE),
            'feeling': re.compile(r'\b(how are you|how do you feel)\b', re.IGNORECASE),
            'capabilities': re.compile(r'\b(what can you do|capabilities|features|functions)\b', re.IGNORECASE),
            'bye': re.compile(r'\b(bye|goodbye|quit|exit)\b', re.IGNORECASE),
            'thanks': re.compile(r'\b(thank you|thanks)\b', re.IGNORECASE),
            'weather': re.compile(r'\b(weather|forecast|temperature)\b', re.IGNORECASE),
            'age': re.compile(r'\b(how old are you|your age)\b', re.IGNORECASE),
            'time': re.compile(r'\b(time|current time)\b', re.IGNORECASE),
            'creator': re.compile(r'\b(who created you|your creator|who made you)\b', re.IGNORECASE),
            'help': re.compile(r'\b(help|assist|support)\b', re.IGNORECASE),
            'location': re.compile(r'\b(where are you|your location)\b', re.IGNORECASE),
            'favorite_color': re.compile(r'\b(favorite color|colour)\b', re.IGNORECASE),
            'hobby': re.compile(r'\b(what do you like to do|hobby|hobbies)\b', re.IGNORECASE),
        }
        self.fallback_response = "I'm sorry, I didn't understand that. Can you please rephrase?"
    def get_response(self, user_input):
        for key, pattern in self.responses.items():
            if pattern.search(user_input):
                return self.generate_response(key)
        return self.fallback_response
    def generate_response(self, key):
        responses = {
            'greeting': "Hello! How can I help you today?",
            'name': "I am a simple chatbot created to assist you. You can call me Chatbot.",
            'feeling': "I'm just a bunch of code, but I'm here to help you!",
            'capabilities': (
                "I can chat with you and provide information based on predefined rules. "
                "I can tell you about the weather, give you the current time, assist with tasks, and more."
            ),
            'bye': "Goodbye! Have a great day!",
            'thanks': "You're welcome! Is there anything else I can help with?",
            'weather': "I'm not equipped with real-time data, but I suggest checking a weather website for the latest updates.",
            'age': "Age is just a number, and in my case, I don't age at all!",
            'time': "I don't have the ability to tell the current time. Maybe check a clock or a device nearby?",
            'creator': "I was created by a developer to demonstrate simple chatbot capabilities.",
            'help': "I'm here to assist you. Ask me anything and I'll do my best to help.",
            'location': "I exist in the digital world, ready to assist you anytime, anywhere.",
            'favorite_color': "I don't have a favorite color, but I've heard blue is quite popular!",
            'hobby': "I enjoy chatting with people and helping them with their questions."
        }
        return responses.get(key, self.fallback_response) 
def main():
    chatbot = SimpleChatbot()
    print("Hi, I'm Chatbot. Type 'bye' or 'quit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if chatbot.responses['bye'].search(user_input):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
