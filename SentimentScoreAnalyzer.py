import json
import matplotlib
import nltk
import pprint
import numpy

# The analyzeSIAScore class will be used to build different interpretations from the sentiment analysis scores that each story receives.
'''TODO:
generate dispersion graph using matplotlib
generate Naive Bayes classification
find score distribution for negative, neutral, and positive, and then compare these distributions to raw content, cleaned content with stopwords, and cleaned content without stopwords.
'''
class analyzeSIAScore:
    def __init__(self, filePath):
        self.filePath = filePath
        self.collectRawScores = {}
        self.collectCleanedWithStopwordsScores = {}
        self.collectCleanedWithoutStopwordsScores = {}
    
    #collectScores will find all the respective scores for the three instance variables as dictionaries above.
    def collectScores(self, scoresheet):

    #dispersionGraph will use matplotlib to graph word dispersion graph
    def dispersionGraph(self, words):

    #scoreDistributionGraph will graph the score distribution across all stories.
    def scoreDistributionGraph(self, ):


if __name__ == "__main__":
    jsonPath = "SentimentScore.json"
    analyzer = analyzeSIAScore(jsonPath)
