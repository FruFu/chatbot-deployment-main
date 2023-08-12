import openai

openai.api_key = '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'  # Replace with your OpenAI API key


def main():


    conversation = [
        {"role": "system", "content": "You are a helpful assistant that provides information about space."},
        {"role": "user", "content": "Hi there! I'm curious about space exploration."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        ai_reply = response.choices[0].message['content']
        print("AI:", ai_reply)
        conversation.append({"role": "assistant", "content": ai_reply})


if __name__ == "__main__":
    main()
