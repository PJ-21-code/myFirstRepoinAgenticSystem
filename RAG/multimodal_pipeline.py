import os
import requests
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

api_key= os.getenv("GROQ_API_KEY")
client= Groq(api_key=api_key)

def speech_to_text(path: Path) -> str:
    with path.open("rb") as audio_file:
        result= client.audio.transcriptions.create(
            file= audio_file,
            model= 'whisper-large-v3',
            response_format="text"
        )

    return result.strip() if isinstance(result, str) else str(result).strip()

def text_summarizer(transcript: str) -> str:
    prompt= (
        "The summary should be in exactly three bullet points."
        "Write only useful facts. Do not invent details. Add point 1). insteaqd of * in bullet points \n\n"
        f"Transcript: {transcript}"
    )

    response= client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=[{'role': 'user','content':prompt}],
        temperature= 0.1
    )

    return response.choices[0].message.content.strip()

def text_to_speech(summary: str, output_file: Path) ->Path:
    speakable= summary.replace("-"," ").replace("\n",". ")

    tts= gTTS(text= speakable, lang="en")
    tts.save(str(output_file))
    return output_file

def main():
    audio_path= Path("sample_voice_note.mp3")
    transcript= speech_to_text(audio_path)
    print("TRANSCRIPT: \n")
    print(f"{transcript} \n")
    print("------------")
    summary= text_summarizer(transcript)
    print("SUMMARY \n" )
    print(f"{summary} \n")
    print("-----------")

    output_path= text_to_speech(summary, Path("spoken_summary.mp3"))
    print(f"Output file is saved as {output_path}")

if __name__ == "__main__":
    main()    