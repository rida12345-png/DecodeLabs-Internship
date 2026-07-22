
import random

responses = {
    "hello":"Hi! How can I help you?",
    "hi":"Hello! 😊",
    "how are you":"I'm doing great!",
    "what is your name":"I'm DecodeLabs Rule-Based Chatbot.",
    "help":"Ask about movies, songs, northern areas, food, books, jokes, AI or Python."
}

exit_commands=["bye","exit","quit","goodbye"]

def get_response(user_input):
    if "movie" in user_input:
        return """🎬 Top 5 Movies
1. Interstellar
2. Inception
3. 3 Idiots
4. The Pursuit of Happyness
5. Avengers: Endgame"""
    elif "song" in user_input or "music" in user_input:
        return """🎵 Top 5 Songs
1. Perfect
2. Until I Found You
3. Night Changes
4. Pasoori
5. Husn"""
    elif "northern" in user_input or "travel" in user_input or "trip" in user_input:
        return """🏔️ Top 5 Northern Areas
1. Hunza Valley
2. Skardu
3. Fairy Meadows
4. Naran Kaghan
5. Swat Valley"""
    elif "food" in user_input or "eat" in user_input:
        return """🍕 Top 5 Foods
1. Biryani
2. Pizza
3. Zinger Burger
4. BBQ
5. Shawarma"""
    elif "book" in user_input:
        return """📚 Top 5 Books
1. Atomic Habits
2. Rich Dad Poor Dad
3. Deep Work
4. Ikigai
5. The Alchemist"""
    elif "joke" in user_input:
        jokes=[
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did Python go to school? To improve its class!",
            "Why was the computer cold? It left its Windows open.",
            "Why do Java developers wear glasses? Because they don't C#.",
            "Why was the programmer broke? Because he used up all his cache."
        ]
        return "😂 Jokes:\n\n" + "\n".join(f"{i+1}. {j}" for i,j in enumerate(jokes))
    elif "python" in user_input:
        return "🐍 Python is beginner-friendly and widely used in AI, Web Development and Automation."
    elif "ai" in user_input:
        return "🤖 AI enables machines to learn and make intelligent decisions."
    elif "motivation" in user_input:
        return "💪 Believe in yourself. Small progress every day leads to big success."
    return responses.get(user_input,"🤔 I don't understand. Try asking about movies, songs, food, books, AI, Python or jokes.")

def chatbot():
    print("="*50)
    print("🤖 DecodeLabs Rule-Based AI Chatbot")
    print("="*50)
    print("Type 'bye' to exit.\n")
    while True:
        user=input("You: ").lower().strip()
        if user in exit_commands:
            print("🤖 Goodbye! Have a great day! 👋")
            break
        print("🤖",get_response(user))
        print()

if __name__=="__main__":
    chatbot()
