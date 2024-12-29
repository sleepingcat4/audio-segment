import os
import json
import subprocess

def segment_audio(json_path, audio_path, output_folder):
    with open(json_path, "r") as f:
        word_timestamps = json.load(f)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, entry in enumerate(word_timestamps):
        start_time = entry["start"]
        end_time = entry["end"]
        word = entry["word"].strip().replace(" ", "_")

        output_file = os.path.join(output_folder, f"{i + 1}_{word}.wav")
        ffmpeg_command = [
            "ffmpeg", "-y", "-i", audio_path,
            "-ss", str(start_time), "-to", str(end_time),
            "-c", "copy", output_file
        ]
        subprocess.run(ffmpeg_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"Word-wise audio segments saved to the folder: {output_folder}")