import asyncio
from openai import AsyncOpenAI

# Set your OpenAI API settings
API_KEY = ""  # Replace with your API key
MODEL = "gpt-3.5-turbo-0125"  # For GPT-4 models you must add at least $5 of extra credits to your account

client = AsyncOpenAI(api_key=API_KEY)

message_history = []

async def main():
    print("Welcome to ChatGPT!")
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'exit':
            print("Goodbye!")
            break
        
        message_history.append({"role": "user", "content": user_input})
        steam = await client.chat.completions.create(
            model=MODEL,
            stream=True,
            messages=message_history)
        
        print("ChatGPT: ", end="")
        response = ""
        async for chunk in steam:
            print(chunk.choices[0].delta.content or "", end="")
            response += chunk.choices[0].delta.content or ""
        message_history.append({"role": "assistant", "content": response})
        print()
        
if __name__ == "__main__":
    asyncio.run(main())
