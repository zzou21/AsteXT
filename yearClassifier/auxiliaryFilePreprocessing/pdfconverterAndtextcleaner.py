'''This file is part of the auxiliary file preprocessing unit. It has three functions -- "pdfToText", "cleanTxt", and "combineToParagraph."
The first reads the content of a PDF and turns it into a txt.
The second cleans the txt and gets rid of unneeded words (this is a very basic cleaning and does NOT substitute cleaning needed before tokenization).
The third combines txt files into a single paragraph (this is usually only used when the paragraph spacing when transforming from PDF to txt is screwed up).
'''
import fitz  # PyMuPDF
import os

def pdfToText(pdfPath):
    document = fitz.open(pdfPath)
    text = ""
    for page_num in range(document.page_count): # This 'for' loop iterates through each page of the PDF
        page = document[page_num]
        text += page.get_text("text")  # Extract text from the page
    return text

def cleanTxt(inputFileName, wordsToRemove):
    # Read the content of the file
    with open(inputFileName, "r", encoding="utf-8") as file:
        content = file.read()
    
    for word in wordsToRemove:
        content = content.replace(word, "")
    with open(inputFileName, "w", encoding="utf-8") as file:
        file.write(content)

def combineToParagraph(inputFile):
    with open(inputFile, "r", encoding="utf-8") as file:
        words = file.readlines()

    #strip newline characters to join with a space
    paragraph = ' '.join(word.strip() for word in words)
    with open(inputFile, "w", encoding="utf-8") as file:
        file.write(paragraph)

if __name__ == "__main__":
    # Path to your PDF file for pdfToText
    inputPDFPath = "/Users/Jerry/Desktop/The Bridegroom by Ha Jin.pdf"
    #Change the directory to where you wish the output txt file of the story you want to store
    outputDirectoryPath = "/Users/Jerry/Desktop"

    # File path to txt for cleanTxt
    inputTxtPath = "/Users/Jerry/Desktop/Aftermath by Mary Yukari Waters_processed.txt"
    #List of words to delete
    wordsToRemove = ["the bridegroom"]

    # File path to txt for combineToParagraph
    inputCombineToParagraph = "/Users/Jerry/Desktop/The Bridegroom by Ha Jin_processed.txt"

    storyName = os.path.basename(inputPDFPath).rsplit(".", 1)[0]
    additionalFileName = "processed"
    outputFileName = f"{storyName}_{additionalFileName}.txt"
    outputFilePath = os.path.join(outputDirectoryPath, outputFileName)

    # Comment out either "text = pdfToText(inputPDFPath)",  "cleanTxt(inputTxtPath, wordsToRemove)", or "combineToParagraph(inputCombineToParagraph)" depending on which one you need to use.

    #text = pdfToText(inputPDFPath)
    #with open(outputFilePath, "w", encoding="utf-8") as text_file:
    #    text_file.write(text)
    #print(f"PDF has been converted to plain text and saved as {outputFilePath}.")
    
    #cleanTxt(inputTxtPath, wordsToRemove)
    #print(f"The words {wordsToRemove} have been removed from {inputTxtPath}.")

    #combineToParagraph(inputCombineToParagraph)