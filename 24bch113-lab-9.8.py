words_to_remove = {"a", "an", "the"}

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        filtered_line = " ".join(word if word.lower() not in words_to_remove else "" for word in line.split())
        outfile.write(filtered_line + "\n")

print("Filtered text file created.")