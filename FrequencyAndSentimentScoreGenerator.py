# Need to fix the Y axis label for dispersion plot.
'''This python class processes the cleaned story content imported from the two JSON files.
Python methods functions in this class:'''
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.sentiment.SentimentIntensityAnalyzer is nltk's pretrained sentiment analyzer.
import json
import matplotlib.pyplot as plt

class nltkProcessing:
    def __init__(self, filePath, key):
        self.filePath = filePath
        self.key = key
        self.tokenized = []
        self.senIntAna = SentimentIntensityAnalyzer()
        self.loadProcess()

    def fileOpenerRead(self, filePath):
        with open(filePath, "r") as file:
            return json.load(file)
    def fileOpenerEdit(self, filePath):
        with open(filePath, "w") as file:
            return json.load(file)
    def loadProcess(self):
        with open(self.filePath, "r") as file:
            storyContent = json.load(file)
        storyContentAsList = storyContent[self.key].split(" ")
        cleanedQuotesStoryContentAsList = [word for word in storyContentAsList if word != "''" and word != "``"]
        cleanedQuotesStoryContentAsString = " ".join(cleanedQuotesStoryContentAsList)
        self.tokenized = nltk.word_tokenize(cleanedQuotesStoryContentAsString)
        #print(cleanedQuotesStoryContentAsString)
        self.textObject = nltk.Text(self.tokenized)
        self.processedContent = cleanedQuotesStoryContentAsString #This stores the processed content so that when a function needs the processed content to be passed through, it could have have access to it.
    def defineConcordance(self, word, width, lines):
        return self.textObject.concordance(word, width=width, lines=lines)
    def defineCollocation(self, nums):
        return self.textObject.collocation_list()[:nums]
    def plotDispersion(self, targets, title="Dispersion Plot"):
        nltk.draw.dispersion.dispersion_plot(self.textObject, targets, title=title)
        plt.show()
    def countWords(self, word):
        return self.tokenized.count(word)
    def collocationGram(self, n, nums):
        NGram = nltk.ngrams(self.tokenized, n)
        frequencyDistri = nltk.FreqDist(NGram)
        return frequencyDistri.most_common(nums)
    def SIA(self, story):
        return self.senIntAna.polarity_scores(story)

if __name__ == "__main__":

    # Change the following three file destinations according to the specific usage context
    StoryCleanedContentSaveStopwords = "StoryContentCleanedSaveStopwords.json"
    StoryCleanedContent = "StoryContentCleaned.json"
    OriginalStory = "RawStoryContent.json"
    # Using different cleaned texts  yields different sentiment analysis scores.
    # Remember to modify the item passed into nltkProcessing in the line below.
    continueOrExit = "Y"
    while continueOrExit == "Y":
        fileFinder = input("Please indicate which JSON file to open: \n1 = Cleaned story content including stopwords\n2 = Cleaned story content excluding stopwords\n3 = Raw story content\nType here: ")
        storyHolder = ""
        if fileFinder == "1":
            storyHolder = "StoryContentCleanedSaveStopwords.json"
            print("Processing using cleaned story content including stopwords....")
        elif fileFinder == "2":
            storyHolder = "StoryContentCleaned.json"
            print("Processing using cleaned story content excluding stopwords....")
        elif fileFinder == "3":
            storyHolder = "RawStoryContent.json"
            print("========\nProcessing using raw story content....\n========")
        else:
            print("Invalid selection.")
        storyFinder = ""
        with open(storyHolder, "r") as file:
            story = json.load(file)
            print("Please type the title of the story to analyze: \n")
            for title in story:
                print(title)
            storySelector = input("\nType story title here: ")
            storyFinder = storySelector
        print("========\nProcessing selected story format....\n========")

        processor = nltkProcessing(storyHolder, storyFinder) # Creating a new nltkProcessing object
        processor.defineConcordance("kreme", width=60, lines=3) #update "kreme" to user input
        collocations = processor.defineCollocation(nums=4)
        print("Most common word combinations:")
        print(collocations)
        target = ["said", "Kreme"] #update target words for dispersion graph
        #processor.plotDispersion(target, title="Word Usage Dispersion Graph")
        countWord = "kreme" #update this to user input
        print("Number of appearances for the word " + countWord + ": ", processor.countWords(countWord))
        collocationGramCombo = processor.collocationGram(3, 3)
        print("\nMost common collections of phrases: ")
        print(collocationGramCombo)

        #sentiment analysis section
        sentimentAnalysis = processor.SIA(processor.processedContent)
        with open("SentimentScore.json", "r") as file:
            scoresheet = json.load(file)
        versionScoreDictionary = {}
        temporaryScoreList = []
        for key, value in sentimentAnalysis.items():
            temporaryScoreList.append(value)
        versionScoreDictionaryStoryName = storyFinder + fileFinder
        versionScoreDictionary[versionScoreDictionaryStoryName] = temporaryScoreList
        if storyFinder not in scoresheet:
            scoresheet[storyFinder] = []
        if versionScoreDictionary not in scoresheet[storyFinder]:
            scoresheet[storyFinder].append(versionScoreDictionary)
        with open("SentimentScore.json", "w") as file:
            json.dump(scoresheet, file, indent=4)
        print(sentimentAnalysis)

        continueOrExit = input("Would you like to continue processing stories?\n(Y/N): ")
    print("========\nProcessing session has been ended\n========")