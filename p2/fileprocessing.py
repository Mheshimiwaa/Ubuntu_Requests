# Part 1: File Processing

# Step 1: Read from input.txt
with open("plp.txt", "r") as infile:
    content = infile.read()

# Step 2: Count words
word_count = len(content.split())

# Step 3: Convert text to uppercase
processed_text = content.upper()

# Step 4: Write results to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("PROCESSED TEXT:\n")
    outfile.write(processed_text + "\n\n")
    outfile.write(f"WORD COUNT: {word_count}\n")

print("✅ Success! 'output.txt' has been created with processed text and word count.")
