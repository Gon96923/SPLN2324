# Read input from lexicon_pt.txt
with open("lexicon_pt.txt", "r") as file:
    content = file.readlines()

new_content = []
for line_number, line in enumerate(content, start=1):
    if line_number >= 7018:
        # Skip lines 7018 and beyond
        continue

    words = line.split()
    new_line = ' '.join(words[:-11]) + '\n'
    new_content.append(new_line)

# Write processed output to lexicon_number.txt
with open("lexicon_number.txt", "w") as file:
    file.writelines(new_content)