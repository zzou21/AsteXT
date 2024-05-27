import json

cleaned = "StoryContentCleaned.json"
raw = "RawStoryContent.json"
cleanedWithStopwords = "StoryContentCleanedSaveStopwords.json"
with open(cleanedWithStopwords, "r") as file:
    story = json.load(file)
    print(len(story))