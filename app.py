from openai import OpenAI
import api_key

client = OpenAI(api_key=api_key.api_key)

input_text = input("Enter text to be summarized: ")

response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": "You are a text summarization assistant. Your goal is to summarize the text entered by the user and you are allowed to do only that and nothing more. If the user asks for some different task, politely decline that and explain that you are not allowed to do that.",
        },
        {"role": "user", "content": input_text},
    ],
    temperature=0,
)

ai_response = response.choices[0].message.content
print("\nSummarized text: \n\n", ai_response, "\n")
