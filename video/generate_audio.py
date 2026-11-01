import asyncio
import subprocess
from pathlib import Path

AUDIO_DIR = Path("/home/sanjayg4/gec-raipur-1991-yearbook/video/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

VOICE = "en-IN-PrabhatNeural"

scenes = [
    {
        "id": "beat1",
        "text": "Hey guys, batch of '91! It’s been 35 years since our final year at GEC Raipur. Look at us right outside the workshop—young, energetic, and terrified of thermo vivas!",
        "rate": "+18%"
    },
    {
        "id": "beat2",
        "text": "Every grain of this 1991 photo is 100% original and untouched—zero AI face distortion. Type any surname—Tiwari, Agrawal, Sinha—and it zooms straight into your face.",
        "rate": "+18%"
    },
    {
        "id": "beat3",
        "text": "Look at the side reels! On the left: the Carnot cycles and lathe tools we sweated over in college. On the right: the robotics, FEA, and space mechanisms we've engineered for 35 years.",
        "rate": "+18%"
    },
    {
        "id": "beat4",
        "text": "Click your face to drop your 2026 city and favorite workshop memory. You can flip into five retro themes—including AutoCAD R11—and export cards to WhatsApp.",
        "rate": "+18%"
    },
    {
        "id": "beat5",
        "text": "It’s completely private for our batch. Open gec-raipur-1991 dot pages dot dev, find your face, and add your story. Cheers to 35 years of Mechanical '91!",
        "rate": "+18%"
    }
]

async def generate_speech():
    import edge_tts
    total_duration = 0
    durations = {}
    for s in scenes:
        out_file = AUDIO_DIR / f"{s['id']}.mp3"
        communicate = edge_tts.Communicate(s["text"], VOICE, rate=s["rate"])
        await communicate.save(str(out_file))
        
        # probe duration
        res = subprocess.run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(out_file)
        ], capture_output=True, text=True)
        dur = float(res.stdout.strip())
        durations[s["id"]] = dur
        total_duration += dur
        print(f"✓ {s['id']}: {dur:.2f}s -> {out_file.name}")
        
    print(f"Total speech duration: {total_duration:.2f}s")
    
    # Save durations metadata
    import json
    with open(AUDIO_DIR / "durations.json", "w") as f:
        json.dump(durations, f, indent=2)

if __name__ == "__main__":
    asyncio.run(generate_speech())
