import os
from langchain.chains.conversation.memory import  ConversationBufferMemory
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = 'API'  # Replace with your OpenAI API key

loader = WebBaseLoader("https://edwardfuportfolio.com/")
index = VectorstoreIndexCreator().from_loaders([loader])


bot_name = "bot"

llm = OpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0,
    max_tokens=256
)
memory = ConversationBufferMemory()
template = """
Erica is an AI pre-sales chatbot working for pxCode. If the AI don't know something just say "I don't know"

Current conversation:
{history}
User: {input}
Erica:"""
PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

conversation = ConversationChain(
    prompt = PROMPT,
    llm=llm,
    verbose=True,
    memory=memory
)

def get_response(msg):

    #print(msg)
    #return conversation.predict(input=msg)
   return index.query(msg,llm=llm)

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
