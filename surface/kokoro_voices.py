"""
Find the best Kokoro voice for Greg.
Generates test phrases across all available voices.
"""
import subprocess, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'kokoro>=0.9', 'soundfile', '--quiet'])

import kokoro, soundfile as sf, os, numpy as np

OUTPUT_DIR = r"D:\Projects\Gregore\surface\voice-samples\kokoro"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PHRASE = "Good morning, David. I've been thinking about something."

print("Loading Kokoro...")
pipeline = kokoro.KPipeline(lang_code='a')

voices = pipeline.voices
print(f"Available voices: {len(voices)}")
for v in sorted(voices):
    print(f"  {v}")

print(f"\nGenerating with each voice...")
for voice_name in sorted(voices):
    try:
        gen = pipeline(PHRASE, voice=voice_name)
        chunks = [c.audio for c in gen]
        if chunks:
            audio = np.concatenate(chunks)
            sf.write(os.path.join(OUTPUT_DIR, f"{voice_name}.wav"), audio, 24000)
            print(f"  {voice_name} -> saved")
    except Exception as e:
        print(f"  {voice_name} -> ERROR: {e}")

print(f"\nDone! Samples in {OUTPUT_DIR}")
