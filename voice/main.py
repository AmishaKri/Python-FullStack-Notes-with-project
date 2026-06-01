import asyncio
import speech_recognition as sr
from openai import OpenAI
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
async_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        instructions="Speak naturally and conversationally.",
        input=speech,
        response_format="pcm",
    ) as response:
       await LocalAudioPlayer().play(response)

def main():
    r = sr.Recognizer() #Speech to text recognizer
    with sr.Microphone() as source: #microphone access
        r.adjust_for_ambient_noise(source) #adjust for ambient noise
        r.pause_threshold = 1
        while True:
            print("Listening...")
            audio = r.listen(source) #listen to the microphone
            print("Recognizing... STT")
            stt_text = r.recognize_google(audio) #recognize the speech
            print(stt_text)
            
            SYSTEM_PROMPT= f"""
                You are an expert voice agent. You are given the transcript of what user has said using voice.
                You need to output as if you are a voice agent and whatever you speak will be converted back to audio using AI and played back to user.
            """
        # Now use OpenAI API for response
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": stt_text}
                ]
            )

            # Open FFMPEG process to play audio
            print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
