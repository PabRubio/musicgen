import os # hi
import numpy as np
import soundfile as sf
from transformers import pipeline
import torch # wut is dis?

os.makedirs("static", exist_ok=True)

PROMPTS = {
    "calm":   "calm ambient pads, soft piano, gentle reverb, relaxing, cinematic",
    "sad":    "slow minor key, sparse piano and soft strings, melancholic, low tempo",
    "happy":  "bright upbeat melody, acoustic guitar, handclaps, cheerful, pop feel",
    "angry":  "aggressive distorted synths and heavy drums, intense, high energy",
    "dreamy": "airy pads, shimmering bells, ethereal, spacious reverb",
}

MAX_NEW_TOKENS = None
torch.set_num_threads(1)

pipe = pipeline(
    "text-to-audio",
    model="facebook/musicgen-small",
    device_map="auto",
)

if MAX_NEW_TOKENS is not None and hasattr(pipe, "model") and hasattr(pipe.model, "generation_config"):
    pipe.model.generation_config.max_new_tokens = int(MAX_NEW_TOKENS)

def generate_and_save(name: str, prompt: str):
    out_path = os.path.join("static", f"{name}.wav")
    print(f"Generating: {name} -> {out_path}")
    result = pipe(prompt) # random inline heheboi :)
    audio = result["audio"] if isinstance(result, dict) else result[0]["audio"]
    sr = result["sampling_rate"] if isinstance(result, dict) else result[0]["sampling_rate"]
    sf.write(out_path, np.array(audio), sr)
    print(f"Saved: {out_path}")

def main():
    for mood, prompt in PROMPTS.items():
        generate_and_save(mood, prompt)
    print("Done. WAVs are in ./static")

if __name__ == "__main__": main()