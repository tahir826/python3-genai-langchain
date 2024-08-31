from langchain.schema import AIMessage, HumanMessage, SystemMessage
conservation = [
    SystemMessage(content="You are helpfull assistant"),
    HumanMessage(content="can you help me in my homework"),
    AIMessage(content="Of course! What Subject do you need help with?"),
    HumanMessage(content="I am struggling with math")
]