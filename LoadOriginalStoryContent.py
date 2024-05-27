import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import contractions

#Change dataFile destination according to the use
dataFile = "RawPrePost2024Joint.json"

def readFile(fileName):
    with open (fileName, "r", encoding="utf-8") as file:
        storyContent = file.read()
        storyContent = "\n".join([paragraph.strip() for paragraph in storyContent.split("\n") if paragraph.strip()])
        storyContent = " ".join([contractions.fix(word) for word in storyContent.split()]) #split words to perform expanding contractions, and then join the individual words in the list back into a string
        storyContent = storyContent.replace("\n", "\n\n")
    return storyContent

def fileSelecter():
    defaultFolder = "StoriesData"
    selectFilePath = filedialog.askopenfilename(initialdir=defaultFolder, filetypes=[("text files", "*.txt")])
    if selectFilePath:
        storyContent = readFile(selectFilePath)
        messagebox.showinfo("Confirmation", "Original story content loaded into JSON.")
        fileName = selectFilePath.split("/")[-1][:-4]
        jsonUpdate(fileName, storyContent)
        return fileName, storyContent
    return None, None

def jsonUpdate(fileNameParam, contentParam):
    with open(dataFile, "r") as file:
        currentFile = json.load(file)
    if fileNameParam not in currentFile:
        currentFile[fileNameParam] = contentParam
    else: 
        print("This story has already been loaded. Select another story.")
    with open(dataFile, "w") as file:
        json.dump(currentFile, file, indent=4, ensure_ascii=False)

window = tk.Tk()
window.title("Select Story to Store Original Content in JSON: ")

fileSelecterButton = tk.Button(window, text="Choose a Text File", command=fileSelecter)
fileSelecterButton.pack(padx=100, pady=20)

window.mainloop()