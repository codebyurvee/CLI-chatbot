import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

messages = [
    {
        "role": "system",
        "content": "You are a helpful coding tutor. Explain things simply.",
    }
]

print("Chatbot ready. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)
