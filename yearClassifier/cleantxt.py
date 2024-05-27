def remove_words_from_file(input_file_path, words_to_remove):
    # Read the content of the file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Remove the specified words
    for word in words_to_remove:
        content = content.replace(word, "")
    
    # Write the modified content back to the same file
    with open(input_file_path, "w", encoding="utf-8") as file:
        file.write(content)

# Example usage
input_file_path = "/Users/Jerry/Desktop/FindingsImpressions copy.txt"  # Path to your input text file
words_to_remove = ["■"]  # List of words to remove

remove_words_from_file(input_file_path, words_to_remove)

print(f"The words {words_to_remove} have been removed from {input_file_path}.")
