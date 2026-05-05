import openai

# Configuration
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")

class MyAI:
    def __init__(self):
        # 2. MEMORY RECALL: This list stores the history of the conversation
        self.memory = [
            {"role": "system", "content": "You are a helpful AI that solves detailed problems and remembers past facts."}
        ]

    def solve_problem(self, user_input):
        # Add the new problem to memory
        self.memory.append({"role": "user", "content": user_input})
        
        try:
            # 1. SOLVE PROBLEM DETAIL: Sending the full memory to the AI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.memory
            )
            
            answer = response.choices[0].message.content
            
            # Save the AI's answer to memory so it can recall it later
            self.memory.append({"role": "assistant", "content": answer})
            
            return answer
        except Exception as e:
            return f"Error: {str(e)}"

# --- Execution ---
bot = MyAI()

print("AI: Hello! I am ready to solve problems and remember our chat.")
while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        break
        
    result = bot.solve_problem(user_query)
    print(f"\nAI: {result}\n")import openai

# Configuration
client = openai.OpenAI(api_key="YOUR_API_KEY_HERE")

class MyAI:
    def __init__(self):
        # 2. MEMORY RECALL: This list stores the history of the conversation
        self.memory = [
            {"role": "system", "content": "You are a helpful AI that solves detailed problems and remembers past facts."}
        ]

    def solve_problem(self, user_input):
        # Add the new problem to memory
        self.memory.append({"role": "user", "content": user_input})
        
        try:
            # 1. SOLVE PROBLEM DETAIL: Sending the full memory to the AI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.memory
            )
            
            answer = response.choices[0].message.content
            
            # Save the AI's answer to memory so it can recall it later
            self.memory.append({"role": "assistant", "content": answer})
            
            return answer
        except Exception as e:
            return f"Error: {str(e)}"

# --- Execution ---
bot = MyAI()

print("AI: Hello! I am ready to solve problems and remember our chat.")
while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        break
        
    result = bot.solve_problem(user_query)
    print(f"\nAI: {result}\n")
