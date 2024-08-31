from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
import os

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_TOKEN")
)
prompt="Translate Hello world to urdu language"
result = llm.invoke(prompt)
print(result)