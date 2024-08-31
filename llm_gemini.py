from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
prompt = PromptTemplate(template="Create a story about {context}",inputVriable=["context"])
chain = prompt | llm
while True :
    human_message = input("Input Your Story Context: ")
    ai_message = chain.invoke({"context": human_message})
    print(ai_message)