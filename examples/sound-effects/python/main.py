import os
from elevenlabs import SoundGenerationSettingsResponseModel
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


def generate_sound_effect(text: str, output_path: str):
    print("Generating sound effects...")

    result = elevenlabs.text_to_sound_effect.convert(
        text=text,
        generation_settings=SoundGenerationSettingsResponseModel(
            duration_seconds=10,  # Optional
            prompt_influence=0.3,  # Optional
        ),
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)

    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    generate_sound_effect("Dog barking", "output.mp3")
