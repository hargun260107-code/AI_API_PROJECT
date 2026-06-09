from google import genai

client = genai.Client(api_key="GEMINI API KEY")

print("AI Chat (type exit to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("AI:", response.text)