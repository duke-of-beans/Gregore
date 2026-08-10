"""
Greg Voice Server — Kokoro TTS with Greg's post-processing.

Runs on G7 as a local HTTP service. The browser surface calls
POST /tts with { "text": "..." } and gets back WAV audio.

Greg's post-processing pipeline:
  1. Pitch shift down (pitch_factor)
  2. High-frequency rolloff ("flumened" consonants)
  3. Dynamic range compression (intimate, not performative)  
  4. Analog hiss (-40dB, Greg's digital signature)
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import io
import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter

# ── Config ──────────────────────────────────────────────────
PORT = 5111
VOICE = None  # Set after running kokoro_voices.py — e.g. 'am_michael'
PITCH_FACTOR = 0.95
PACE_FACTOR = 0.94
LOWPASS_BLEND = 0.80  # 80% filtered, 20% original
HISS_DB = -40

# ── Load Kokoro ─────────────────────────────────────────────
import kokoro
pipeline = None

def init():
    global pipeline, VOICE
    print("[tts] Loading Kokoro...")
    pipeline = kokoro.KPipeline(lang_code='a')
    
    # Auto-select voice if not set
    if not VOICE:
        voices = sorted(pipeline.voices)
        # Prefer male voices
        male_voices = [v for v in voices if v.startswith('am_')]
        VOICE = male_voices[0] if male_voices else voices[0]
    
    print(f"[tts] Voice: {VOICE}")
    print(f"[tts] Post-processing: pitch={PITCH_FACTOR}, pace={PACE_FACTOR}, "
          f"lowpass={LOWPASS_BLEND}, hiss={HISS_DB}dB")

def generate(text: str) -> bytes:
    """Generate Greg-voiced audio from text."""
    gen = pipeline(text, voice=VOICE)
    chunks = [c.audio for c in gen]
    if not chunks:
        return b''
    
    audio = np.concatenate(chunks).astype(np.float64)
    sr = 24000
    
    # ── Post-processing pipeline ────────────────────────────
    
    # 1. Pitch shift
    stretched = np.interp(
        np.linspace(0, len(audio), int(len(audio) / PITCH_FACTOR)),
        np.arange(len(audio)), audio
    )
    if len(stretched) > len(audio):
        stretched = stretched[:len(audio)]
    else:
        stretched = np.pad(stretched, (0, len(audio) - len(stretched)))
    audio = stretched
    
    # 2. Pace slowdown
    slowed = np.interp(
        np.linspace(0, len(audio), int(len(audio) / PACE_FACTOR)),
        np.arange(len(audio)), audio
    )
    audio = slowed
    
    # 3. HF rolloff (flumened)
    nyq = sr / 2
    cutoff = 5000 / nyq
    if cutoff < 1.0:
        b, a = butter(1, cutoff, btype='low')
        filtered = lfilter(b, a, audio)
        audio = LOWPASS_BLEND * filtered + (1 - LOWPASS_BLEND) * audio
    
    # 4. Dynamic range compression
    threshold = 0.3
    ratio = 3.0
    abs_audio = np.abs(audio)
    mask = abs_audio > threshold
    compressed = audio.copy()
    compressed[mask] = np.sign(audio[mask]) * (
        threshold + (abs_audio[mask] - threshold) / ratio
    )
    audio = compressed
    
    # 5. Analog hiss
    noise_level = 10 ** (HISS_DB / 20)
    noise = np.random.randn(len(audio)) * noise_level
    if 8000 / nyq < 1.0:
        b_bp, a_bp = butter(2, [8000/nyq, min(16000/nyq, 0.99)], btype='band')
        noise = lfilter(b_bp, a_bp, noise)
    audio = audio + noise
    
    # 6. Normalize
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio / peak * 0.95
    
    # Encode as WAV
    buf = io.BytesIO()
    sf.write(buf, audio.astype(np.float32), sr, format='WAV')
    return buf.getvalue()

# ── HTTP Server ─────────────────────────────────────────────

class TTSHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/tts':
            self.send_error(404)
            return
        
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        text = body.get('text', '')
        
        if not text:
            self.send_error(400, 'Missing text')
            return
        
        print(f"[tts] Generating: \"{text[:60]}\"")
        wav_data = generate(text)
        
        self.send_response(200)
        self.send_header('Content-Type', 'audio/wav')
        self.send_header('Content-Length', str(len(wav_data)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(wav_data)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        pass  # suppress default logging

if __name__ == '__main__':
    init()
    server = HTTPServer(('0.0.0.0', PORT), TTSHandler)
    print(f"[tts] Greg Voice Server running on http://localhost:{PORT}/tts")
    print(f"[tts] POST /tts {{ \"text\": \"Hello\" }} -> WAV audio")
    server.serve_forever()
