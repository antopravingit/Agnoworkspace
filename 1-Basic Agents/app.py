from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


agent=Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an assistant please reply based on the user queries",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("What is the latest score of India vs News Zealand CT 2025 final",stream=True)