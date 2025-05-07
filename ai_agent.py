import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage

from langgraph.prebuilt import create_react_agent

load_dotenv()

gq_key = os.environ.get("GROQ_API_KEY")
tvly_key = os.environ.get("TVLY_API_KEY")
openai_key = os.environ.get("OPENAI_API_KEY")

search_tool = TavilySearchResults(max_results=2)

def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):


    if provider == "groq":
        llm = groq_llm = ChatGroq(model=llm_id)
    else:
        llm =  ChatOpenAI(model=llm_id)

    system_prompt = "Act as AI chatbot"
    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model =groq_llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state = {"message":query}

    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message,AIMessage)]
    print("asdf",ai_message)
    return ai_message[-1]