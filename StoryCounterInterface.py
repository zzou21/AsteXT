'''This file allows the user to select a story file (all stored as txt files) and check the word count of the selected story.

Currently, the "defaultFolder" is set to "StoriesData". Change this variable in the fileSelectorInterface function accordingly.
'''
import tkinter as tk
import string
from tkinter import filedialog
from tkinter import messagebox
import json

# Change the dataFile destination according to the specific usage context
dataFile = "StoryMetadata.json"

def wordCounter(fileName):
    wordCounterInt = 0
    with open(fileName, "r") as file:
        fileContent = file.read()

        # The line below replaces hyphens with spaces so that the program doesn't count words on either side of a hyphen as one word.
        fileContent = fileContent.replace("-", " ")

        fileContent = "".join(word for word in fileContent if word not in string.punctuation)
        processedFileContent = fileContent.split()
        wordCounterInt = len(processedFileContent)
    return wordCounterInt

def fileSelectorInterface():
    defaultFolder = "StoriesData"
    selectFilePath = filedialog.askopenfilename(initialdir=defaultFolder, filetypes=[("Text files", "*.txt")])
    if selectFilePath:
        wordCount = wordCounter(selectFilePath)
        messagebox.showinfo("Story Word Count", f"The story contains {wordCount} words.")
        
        # This line turns selectFilePath (which returns the entire path of the selected file, into just the file name, which is the last value in the file path). Returning "fileName[;-4]" gets rid of the ".txt" suffix that take up the last 4 indices of the fileName string.
        fileName = selectFilePath.split("/")[-1][:-4]
        jsonUpdate(fileName, wordCount)
        return fileName, wordCount
    return None, None

# This function stores the story name and its metadata into a json file.
'''JSON file template:
key: string of story file name without .txt suffix
value: list -> [word count, author, year, journal]
'''
def jsonUpdate(fileNameParam, wordCountParam):
    with open(dataFile, "r") as file:
        existingStories = json.load(file)
    if fileNameParam not in existingStories:
        existingStories[fileNameParam] = []
        existingStories[fileNameParam].append(wordCountParam)
    with open(dataFile, "w") as file:
        json.dump(existingStories, file)

window = tk.Tk()
window.title("Select Story File to Process Metadata")

fileSelecterButton = tk.Button(window, text="Choose a Text File", command=fileSelectorInterface)
fileSelecterButton.pack(padx=100, pady=20)

#displaySelectedFile = tk.Label(window, text="Selected Story:")
#displaySelectedFile.pack()
#fileText = tk.Text(window, wrap=tk.WORD, height=10, width=40)
#fileText.pack(padx=20, pady=20)

window.mainloop()