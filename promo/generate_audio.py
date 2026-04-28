"""Generate per-segment narration audio and output durations for Manim sync."""
import json
from gtts import gTTS
from mutagen.mp3 import MP3

SEGMENTS = [
    {"id": "intro", "text": "Introducing eHardware. Hardware Designs and Products."},
    {"id": "f1", "text": "Feature one. PCB Design Library. Production-ready schematics and layouts for common embedded platforms."},
    {"id": "f2", "text": "Feature two. FPGA Reference Designs. Synthesizable HDL for Xilinx and Lattice FPGAs with testbenches."},
    {"id": "f3", "text": "Feature three. Manufacturing Automation. Automated BOM generation, DRC checks, and Gerber export pipelines."},
    {"id": "arch", "text": "Under the hood, eHardware is built with KiCad, Verilog, Python. The architecture flows from Schematic, to Layout, to DRC, to BOM Gen, to Gerber Export."},
    {"id": "cta", "text": "eHardware. Open source and production ready. Visit github dot com slash embeddedos-org slash eHardware-Designs-Products."},
]

durations = {}
audio_files = []

for seg in SEGMENTS:
    filename = f"seg_{seg['id']}.mp3"
    tts = gTTS(text=seg["text"], lang="en", slow=False)
    tts.save(filename)
    dur = MP3(filename).info.length
    durations[seg["id"]] = round(dur + 0.5, 1)  # add 0.5s padding
    audio_files.append(filename)
    print(f"  {seg['id']}: {dur:.1f}s -> padded {durations[seg['id']]}s")

# Write durations JSON for Manim to read
with open("durations.json", "w") as f:
    json.dump(durations, f, indent=2)

# Concatenate all segments into single narration.mp3
import subprocess
list_file = "concat_list.txt"
with open(list_file, "w") as f:
    for af in audio_files:
        f.write(f"file '{af}'\n")

subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", list_file, "-c", "copy", "narration.mp3"
], check=True)

total = sum(durations.values())
print(f"\nTotal narration: {total:.1f}s")
print(f"Durations: {json.dumps(durations)}")
