'''Applying the year classifier BERT model.'''
print("Importing libraries and model...")
import torch
from transformers import BertForSequenceClassification
from transformers import AutoTokenizer

modelPath = "yearClassifier/modelTrained"
newModel = BertForSequenceClassification.from_pretrained(modelPath)
newTokenizer = AutoTokenizer.from_pretrained(modelPath)
newModel.eval()
print("Libraries and model imported.")

def predictInputYear(story, model, tokenizer, threshold=0.5):
    inputStory = tokenizer(story, return_tensors="pt", padding="max_length", truncation=True, max_length=256)
    operatingDevice = torch.device("cuda" if torch.cuda.is_available() else "cpu") # cuda -> gpu
    model.to(operatingDevice)
    inputStory = {key: value.to(model.device) for key, value in inputStory.items()}
    with torch.no_grad():
        outputs = model(**inputStory)
        logits = outputs.logits
    # getting probabilities
    probabilities = torch.sigmoid(logits).cpu().numpy().flatten()
    
    # Use 0.5 threshold for binary classification
    label = 1 if probabilities[1] > threshold else 0
    if label == 1:
        return {"Context": "After 2014", "probability": probabilities[1]}
    else:
        return {"Context": "Before 2014", "probability": probabilities[0]}

print("Calculating inputted story...")
newStoryFilePath = "/Users/Jerry/Desktop/DH proj:reading/Asian American short story project/For testing MrsTsubaki.txt"
with open(newStoryFilePath, "r") as file:
    content = file.read()

storyInput = content
resultPrediction = predictInputYear(storyInput, newModel, newTokenizer)
print("Calculation finished.")
print("PREDICTION RESULT", resultPrediction)