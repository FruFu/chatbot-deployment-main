import os
import torch
import openai
from langchain.chains.conversation.memory import  ConversationBufferMemory
from langchain import OpenAI
from langchain.chains import ConversationChain


os.environ['OPENAI_API_KEY'] = ''  # Replace with your OpenAI API key
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

bot_name = "bot"

llm = OpenAI(
    model_name='text-davinci-003',
    temperature=0,
    max_tokens=256
)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory
)

def get_response(msg):


    ai_reply = conversation.predict(input=msg)
    return ai_reply

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
