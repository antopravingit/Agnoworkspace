import os
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from openai import OpenAI
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import Toolkit

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create a custom tool for audio transcription
class AudioTranscriptionTool(Toolkit):
    def __init__(self, base_dir: Optional[Path] = None):
        super().__init__(name="audio_transcription")
        self.base_dir = base_dir or Path.cwd()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Register the methods as tools
        self.register(self.transcribe)
    
    def transcribe(self, file_name: str) -> str:
        """
        Transcribe an audio file using OpenAI Whisper API.
        
        Args:
            file_name (str): The name of the audio file to transcribe.
            
        Returns:
            str: The transcribed text.
        """
        try:
            file_path = self.base_dir / file_name
            
            with open(file_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            
            return transcription.text
        except Exception as e:
            return f"Error transcribing audio: {str(e)}"
    
# Define a directory to look for audio files
audio_dir = Path.cwd()  # Current directory, change as needed

# Create an Agno agent with the custom audio transcription tool
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="I am an assistant that can transcribe and analyze audio content.",
    instructions=[
        "Use the audio_transcription.transcribe tool to transcribe audio files.",
        "After transcribing, you can analyze the content of the transcription."
    ],
    tools=[AudioTranscriptionTool(base_dir=audio_dir)],
    markdown=True
)

# Example usage
agent.print_response(
    "Please transcribe 'Order-Processing-Audio.mp3' and provide a summary of the conversation.",
    stream=True
)