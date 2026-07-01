import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Say hello from Career Genie"}
    ]
)

print(response["message"]["content"])