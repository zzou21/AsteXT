import nltk
import contractions
from nltk.tokenize import TweetTokenizer
import pprint


'''
with open("HistoryCoding/HIST510S/StoriesData/AGNI/DonutMan.txt", "r") as file:
    fileContent = file.read()
    

storyTokenize = TweetTokenizer().tokenize(fileContent)

#storyTokenize = nltk.word_tokenize(fileContent)

storyLetters = [word for word in storyTokenize if word.isalpha()]

print(storyLetters)
'''

'''
words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
#print(words)
stopwords = nltk.corpus.stopwords.words("english")
#print(stopwords)
wordsWithoutStopwords = [word for word in nltk.corpus.state_union.words() if words not in stopwords]
#print(wordsWithoutStopwords)

text = 
#pprint(nltk.word_tokenize(text), width=79, compact=True)

words: list[str] = nltk.word_tokenize(text)
fd = nltk.FreqDist(words)
#fd.tabulate(10)
print(fd.most_common(10))
'''

'''
nltk.download([
"names",
"stopwords",
"state_union",
"twitter_samples",
"movie_reviews",
"averaged_perceptron_tagger",
"vader_lexicon",
"punkt",
"wordnet"
])
'''