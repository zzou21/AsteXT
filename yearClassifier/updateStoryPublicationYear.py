# This file has two functions. "yearStory" turns  json files that store stories in the format storyname:storycontent to publicationyear:storycontent. "combineJsons" combine two JSON files -- one storytitle:storycontent and the other storytitle:publicationyear -- into publicationyear:storycontent.

import json

def yearStory(originalJson, destinationJson):
    storyNamesAndYears = {}
    existingNamesAndYears = {}
    with open(destinationJson, "r") as fileYears:
        temporaryHolder = json.load(fileYears)
        if not temporaryHolder:
            print("Current JSON file empty. Input new title:year pairs.")
            existingNamesAndYears = {}
        else:
            print("existing", existingNamesAndYears)
            existingNamesAndYears.update(temporaryHolder)
            
    with open(originalJson, "r") as fileStories:
        storiesContent = json.load(fileStories)
        for title, story in storiesContent.items():
            if title not in existingNamesAndYears:
                year = input(f"Enter the publication year of the story {title}: ")
                storyNamesAndYears[title] = int(year)
                print(storyNamesAndYears)

    if not storyNamesAndYears:
        print("All stories have been assigned a publication year.")
    else:
        print("Adding story publication years to JSON file...")
        existingNamesAndYears.update(storyNamesAndYears)
        print(existingNamesAndYears)
        with open("yearClassifier/storyPublicationYear.json", "w") as fileYears:
            json.dump(existingNamesAndYears, fileYears, indent=4)
        print("Story publication years added.")

def combineJsons (titleStory, titleYear, destinationJson):
    titleStoryDictionary = {}
    titleYearDictionary = {}
    with open(titleStory, "r") as fileTitle:
        titleStoryDictionary = json.load(fileTitle)
    with open(titleYear, "r") as fileYear:
        titleYearDictionary = json.load(fileYear)
    
    combined = {titleYearDictionary[key]: titleStoryDictionary[key] for key in titleYearDictionary if key in titleStoryDictionary}
    with open(destinationJson, "w") as fileCombined:
        json.dump(combined, fileCombined, indent=4)

if __name__ == "__main__":
    originalPath = "RawPrePost2014.json"
    destinationPath = "yearClassifier/storyPublicationYear.json"
    combinedDestination = "yearClassifier/publicationYearStory.json"

    # comment/Un-comment one of the below function calls based on need. 

    #yearStory(originalPath, destinationPath)
    combineJsons(originalPath, destinationPath, combinedDestination)