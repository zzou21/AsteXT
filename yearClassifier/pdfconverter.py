import fitz  # PyMuPDF

def pdf_to_text(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Loop through each page
    for page_num in range(document.page_count):
        page = document[page_num]
        text += page.get_text("text")  # Extract text from the page

    return text

# Path to your PDF file
pdf_path = "/Users/Jerry/Desktop/The Bridegroom.pdf"

# Convert PDF to text
text = pdf_to_text(pdf_path)

# Save the text to a .txt file
with open("/Users/Jerry/Desktop/Aftermath copy.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)

print("PDF has been converted to plain text and saved as 'output.txt'")
