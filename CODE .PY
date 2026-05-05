import openai
import json

# Configuration
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")

class GamingFinanceAI:
    def __init__(self):
        # SYSTEM PROMPT: This defines the AI's "Personality" and "Knowledge"
        # We add Free Fire, BGMI, GTA 5, Roblox, and Share Market instructions here.
        self.memory = [
            {
                "role": "system", 
                "content": (
                    "You are 'My Life App' AI. You are a pro gamer and financial advisor. "
                    "1. Pro Gaming: Provide tricks, sensitivity settings, and map strategies for Free Fire, "
                    "BGMI, GTA 5, and Roblox. "
                    "2. Share Market: Provide detailed analysis of stocks, market trends, and investment tips. "
                    "3. Memory: Always refer to previous game scores or stock picks mentioned by the user."
                )
            }
        ]

    def get_market_data(self, stock_symbol):
        """
        EXTRA FUNCTION: In a real app, you would connect this to a 
        finance API (like Yahoo Finance). For now, it simulates the logic.
        """
        return f"Fetching real-time data for {stock_symbol}... Market is currently Bullish."

    def chat(self, user_input):
        # 2. MEMORY RECALL: Append user input to history
        self.memory.append({"role": "user", "content": user_input})
        
        try:
            # 1. SOLVE PROBLEM DETAIL
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.memory,
                temperature=0.7 # Makes the AI a bit more creative for gaming tips
            )
            
            answer = response.choices[0].message.content
            self.memory.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            return f"Error: {str(e)}"

# --- Execution ---
bot = GamingFinanceAI()

print("--- My Life App: Gaming & Finance Edition ---")
print("Ask me about Free Fire settings, GTA 5 cheats, or Stock Market tips!")

while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        break
    
    # Logic to trigger the 'Extra Function' for Share Market
    if "stock" in user_query.lower() or "market" in user_query.lower():
        print(f"System: {bot.get_market_data('Global Indices')}")
        
    result = bot.chat(user_query)
    print(f"\nAI: {result}\n")
