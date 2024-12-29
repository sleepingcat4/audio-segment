import whisper
import json

model = whisper.load_model("tiny")
result = model.transcribe("audio.wav", word_timestamps=True)

words_with_timestamps = []

for segment in result["segments"]:
    for word_info in segment["words"]:
        words_with_timestamps.append({
            "word": word_info["word"],
            "start": word_info["start"],
            "end": word_info["end"]
        })

with open("word_timestamps.json", "w") as f:
    json.dump(words_with_timestamps, f, indent=4)

print("Word-level timestamps saved to 'word_timestamps.json'")