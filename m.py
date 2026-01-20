import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

print("API KEY loaded:", "YES" if os.getenv("OPENAI_API_KEY") else "NO")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("AI Chatbot Assistant")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break


    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        print("AI:", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)

