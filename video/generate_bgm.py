import numpy as np
import scipy.io.wavfile as wav
import subprocess
from pathlib import Path

# Parameters
sr = 44100
duration = 70.0
t = np.linspace(0, duration, int(sr * duration), False)

# Warm nostalgic chord progression (BPM 72, 4 beats per chord = 3.33s per chord)
# C major 9 (C4, E4, G4, B4, D5) -> Am9 (A3, C4, E4, G4, B4) -> Fmaj9 (F3, A3, C4, E4, G4) -> Gsus4/G (G3, C4, D4, G4, B4)
chords = [
    [261.63, 329.63, 392.00, 493.88, 587.33], # Cmaj9
    [220.00, 261.63, 329.63, 392.00, 493.88], # Am9
    [174.61, 220.00, 261.63, 329.63, 392.00], # Fmaj9
    [196.00, 261.63, 293.66, 392.00, 493.88], # G6/9
]

chord_duration = 3.333
signal = np.zeros_like(t)

# Generate layered gentle electric piano / warm ambient pad
for i in range(int(duration / chord_duration) + 1):
    chord_start = i * chord_duration
    chord = chords[i % len(chords)]
    chord_t_idx = (t >= chord_start) & (t < chord_start + chord_duration + 1.5)
    chord_t = t[chord_t_idx] - chord_start
    
    chord_wave = np.zeros_like(chord_t)
    for note_idx, freq in enumerate(chord):
        # fundamental + soft harmonics
        decay = np.exp(-chord_t / 3.0)
        h1 = np.sin(2 * np.pi * freq * chord_t) * decay
        h2 = 0.3 * np.sin(2 * np.pi * freq * 2 * chord_t) * np.exp(-chord_t / 1.5)
        h3 = 0.1 * np.sin(2 * np.pi * freq * 3 * chord_t) * np.exp(-chord_t / 0.8)
        # soft stereo spread simulation
        chord_wave += (h1 + h2 + h3) * 0.15
        
    signal[chord_t_idx] += chord_wave

# Fade in and fade out
fade_in = int(sr * 2.0)
fade_out = int(sr * 3.0)
signal[:fade_in] *= np.linspace(0, 1, fade_in)
signal[-fade_out:] *= np.linspace(1, 0, fade_out)

# Normalize volume to subtle background level (-22 dB RMS)
max_val = np.max(np.abs(signal))
if max_val > 0:
    signal = signal / max_val * 0.18 # keep soft so voiceover sits proudly on top

wav_path = "/home/sanjayg4/gec-raipur-1991-yearbook/video/hf-project/assets/bg_music.wav"
wav.write(wav_path, sr, (signal * 32767).astype(np.int16))

mp3_path = "/home/sanjayg4/gec-raipur-1991-yearbook/video/hf-project/assets/bg_music.mp3"
subprocess.run(["ffmpeg", "-y", "-i", wav_path, "-b:a", "192k", mp3_path], capture_output=True)
print(f"BGM generated successfully: {mp3_path}")
