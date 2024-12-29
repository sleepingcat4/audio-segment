import os

def save_word(folder_path, output_txt):
    word_names = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".wav"):
            word = file_name.split('_', 1)[1].replace(".wav", "")
            word_names.append(word)

    with open(output_txt, "w") as f:
        for word in word_names:
            f.write(f"{word}\n")

    print(f"Word names saved to '{output_txt}'")