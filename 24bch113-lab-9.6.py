with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    merged_lines = [l for pair in zip(lines1, lines2) for l in pair]
    merged_lines += lines1[len(lines2):] + lines2[len(lines1):]  # Remaining lines
    out.writelines(merged_lines)

print("Files merged successfully.")