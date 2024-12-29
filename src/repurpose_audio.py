import os
import subprocess

def get_audio_files_for_words(segment_folder, words):
    audio_files = []
    for word in words:
        word = word.strip().lower()
        for file in os.listdir(segment_folder):
            if file.endswith(".wav") and word in file.lower():
                audio_files.append(os.path.join(segment_folder, file))
                break
    return audio_files

def audio_repurpose(segment_folder, passage, output_audio):
    words = passage.split()
    audio_files_for_words = get_audio_files_for_words(segment_folder, words)
    if not audio_files_for_words:
        print("No matching audio files found!")
        return
    input_files = "\n".join([f"file '{file}'" for file in audio_files_for_words])
    with open("input_files.txt", "w") as f:
        f.write(input_files)
    ffmpeg_command = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "input_files.txt",
        "-c", "pcm_s16le", "-ar", "44100", "-ac", "2", output_audio
    ]
    subprocess.run(ffmpeg_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove("input_files.txt")
    print(f"Sentence audio saved to '{output_audio}'")
    return Audio(output_audio)