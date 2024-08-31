from langchain_openai import OpenAI


from dotenv import load_dotenv
load_dotenv()
import os
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
prompt = "Translate This text to urdu Hi I am using whatsapp"
response = llm.invoke(prompt)
print(response)