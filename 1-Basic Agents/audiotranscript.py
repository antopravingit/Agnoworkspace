import httpx
from agno.agent import Agent
from agno.media import Audio
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="mistral-saba-24b"),
    markdown=True
)

#url ="https://agno-public.s3.us-east-1.amazonaws.com/demo_data/QA-01.mp3"
#url ="https://outsourcey.com/wp-content/uploads/2024/10/Order-Processing-Audio-Sample-English-Diana-Cause-_-Jemima-VEED.mp3"
#url = "https://www.bruntwork.co/wp-content/uploads/2023/03/Inbound-sales-audio-sample.mp3"

#response = httpx.get(url)
#audio_content = response.content

local_audio_file_path =r".\Order-Processing-Audio.mp3"

# Read the local audio file
with open(local_audio_file_path, "rb") as audio_file:
    audio_content = audio_file.read()

agent.print_response(
    "Give a transcript of this audio conversation. Use speaker A, speaker B to identify speakers.",
    audio=[Audio(content=audio_content)],
    stream=True,
)