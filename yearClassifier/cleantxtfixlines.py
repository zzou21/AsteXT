def convert_to_paragraph(input_file_path):
    # Read the content of the file
    with open(input_file_path, "r", encoding="utf-8") as file:
        words = file.readlines()
    
    # Strip newline characters and join words with a space
    paragraph = ' '.join(word.strip() for word in words)

    
    # Write the paragraph back to the file
    with open(input_file_path, "w", encoding="utf-8") as file:
        file.write(paragraph)

# Example usage
input_file_path = "/Users/Jerry/Desktop/Accomplice copy.txt"  # Path to your input text file

convert_to_paragraph(input_file_path)

print(f"The words have been combined into a paragraph and saved to.")
