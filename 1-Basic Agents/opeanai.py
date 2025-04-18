from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mlx_transcribe import MLXTranscribeTools
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Get audio files from storage/audio directory
agno_root_dir = Path(__file__).parent.parent.parent.resolve()
audio_storage_dir = agno_root_dir.joinpath("storage/audio")
if not audio_storage_dir.exists():
    audio_storage_dir.mkdir(exist_ok=True, parents=True)

agent = Agent(
    name="Transcription Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[MLXTranscribeTools(base_dir=audio_storage_dir)],
    instructions=[
        "To transcribe an audio file, use the `transcribe` tool with the name of the audio file as the argument.",
        "You can find all available audio files using the `read_files` tool.",
    ],
    markdown=True,
)

agent.print_response("Summarize the reid hoffman ted talk, split into sections", stream=True)