# This file is for code testing purposes.

storyDataJsonPath = "publicationYearStory.json"
with open(storyDataJsonPath, "r") as file:
    storyData = json.load(file)
dataset = [{"story": story, "year": int(year)} for year, story in storyData.items()]
for story in dataset:
    story["label"] = 1 if story["year"] >2004 else 0
print(dataset)

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
def tokenizeStories(stories):
    return tokenizer(stories["story"], padding="max_length", truncation=True, max_length=256)

tokenizedStories = [tokenizeStories(storyItem) for storyItem in dataset]
print(tokenizedStories)
def formatData(tokenizedStories):
    return{
        "input_ids": torch.tensor(tokenizedStories["input_ids"]),
        "attentionMask": torch.tensor(tokenizedStories["attention_mask"]),
        "label": torch.tensor(tokenizedStories["label"])
    }
formattedData = [formatData(terms) for terms in formatData(tokenizedStories)]
