def categorize_value(value):
    if -4 <= value < -0.8:
        return "NEGATIVE\n"
    elif -0.8 <= value <= 0.8:
        return "NEUTRAL\n"
    elif 0.8 < value <= 4:
        return "POSITIVE\n"
    else:
        return "UNKNOWN\n"

def process_line(line):
    columns = line.split()  # Split line by spaces
    if len(columns) >= 2:
        word, num = columns[-2], float(columns[-1])
        category = categorize_value(num)
        return f"{word}:{category}"
    else:
        return line

# Read input from lexicon_number.txt
with open("lexicon_number.txt", "r") as file2:
    content2 = file2.readlines()

new_content2 = []
for line in content2:
    processed_line = process_line(line)
    new_content2.append(processed_line)

# Write categorized output to lexicon_category.txt
with open("lexicon_category.txt", "w") as file3:
    file3.writelines(new_content2)
