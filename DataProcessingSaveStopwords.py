#Same code as DataProcessing.py except this one does NOT remove stopwords.

'''This file cleans and processes raw story txt files throuhg tokenization, removing punctuations, expanding contractions, and other methods. After a story selected by the user has been cleaned, the story is stored in a JSON file, with the story name as the key.
'''
from tkinter import filedialog
from tkinter import messagebox
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
#from nltk.corpus import stopwords
import contractions
import tkinter as tk
import json
import re
import string
import unidecode
#import word2number, pycontractions, gensim.downloader as api

dataFile = "StoryContentCleanedSaveStopwords.json"
'''Types of data cleaning to go through:
contraction, remove punctuation, remove stopwords, convert to lowercase, convert words to numerical numbers, stemming and lemmatization
'''
class StoryProcessorSaveStopwords:
    def __init__ (self):
        self.lemmatizer = WordNetLemmatizer() #lemmatizer. When calling it in future functions, need to include .lemmatize
        self.removePunctuation = str.maketrans("", "", string.punctuation) #finds punctuations
        #self.stopWords = set(stopwords.words("english"))
        #finds stopwords in the English language
    
    def process(self, storyContent):
        processedStory = []
        storyContent = re.sub(" +", " ", storyContent) #replaces multiple blank spaces with just one
        storyContent = storyContent.lower() #lowercase all spelling
        storyContent = " ".join([contractions.fix(word) for word in storyContent.split()]) #split words to perform expanding contractions, and then join the individual words in the list back into a string
        storySentences = sent_tokenize(storyContent) #tolenize the entire story into sentences, with each sentence being a token
        for sentence in storySentences:
            sentence = sentence.translate(self.removePunctuation) #removes punctuation
            sentence = sentence.strip() #removes blank spaces
            sentence = unidecode.unidecode(sentence) #represent special characters in ASCII characters
            sentence = sentence.replace(u"‘", "'").replace(u"’", "'")
            sentence = sentence.replace(u"“", '"').replace(u"”", '"')
            sentence = sentence.replace("``", '"').replace("''", '"')  # Replace any grave accents used incorrectly
            sentence = sentence.replace("``", "\n\n")
            individualWords = word_tokenize(sentence) #tokenize sentences into words, with each sentence being one token
            lemmatizedAndStopwordRemoved = " ".join([self.lemmatizer.lemmatize(word) for word in individualWords]) #first remove words that are stop words, then lemmatize the remaining words back to their original forms, such as "drove" to "drive"
            processedStory.append(lemmatizedAndStopwordRemoved)
        return " ".join(processedStory)

def fileSelecterForContraction():
    textProcessor = StoryProcessorSaveStopwords()
    defaultFolder = "StoriesData"
    selectFilePath = filedialog.askopenfilename(initialdir=defaultFolder, filetypes=[("Text files", "*.txt")])
    with open(selectFilePath, "r", encoding="utf-8") as file:
        fileReader = file.read()
    fileName = selectFilePath.split("/")[-1][:-4]

    if selectFilePath:
        contractionResult = textProcessor.process(fileReader)
        messagebox.showinfo("Preview.", f"Cleaning of " + fileName + " is completed. \nFirst 100 characters post-cleaning preview: \n\n<<\n " + contractionResult[:100] + "\n" + ">>")
        
        # This line turns selectFilePath (which returns the entire path of the selected file, into just the file name, which is the last value in the file path). Returning "fileName[;-4]" gets rid of the ".txt" suffix that take up the last 4 indices of the fileName string.
        jsonUpdate(fileName, contractionResult)
        return fileName, contractionResult
    return None, None

def jsonUpdate(fileNameParam, contractionResultParm):
    with open(dataFile, "r") as file:
        existingContractions = json.load(file)
    if fileNameParam not in existingContractions:
        existingContractions[fileNameParam] = contractionResultParm
    with open(dataFile, "w") as file:
        json.dump(existingContractions, file, indent=4)

cleaningAndProcessingWindow = tk.Tk()
cleaningAndProcessingWindow.title("Select Story to Clean and Process")

instruction_label = tk.Label(cleaningAndProcessingWindow, text="Note: This data cleaning and processing function will perform tasks including: \n\n- removing punctuation;\n- lowercasing all spelling;\n- expand contractions;\n- remove blank spaces;\nand others.\n\nThe processed story content will be stored in a JSON dictionary file in which the story title is the key and the story content being the value.", anchor="w", justify="left")
instruction_label.pack(pady=(60, 10))

fileSelectorButton = tk.Button(cleaningAndProcessingWindow, text="Choose a Story File", command=fileSelecterForContraction)
fileSelectorButton.pack(padx=20, pady=20)

cleaningAndProcessingWindow.mainloop()