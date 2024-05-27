# If there is a need to combine multiple JSON files together (such as store different groups of stories together), one could use this program to do so:
import json

# Put in this list all the pathnames of the JSON files that need to be combined together
json_files = ["RawPre2014.json", "RawStoryContent.json"]
python_objects = {}
for json_file in json_files:
    with open(json_file, "r") as f:
        python_objects.update(json.load(f))

#Create a new JSON file (don't forget to add the {} sign in the new file!!) and add the path name here
with open("CombinedPrePost2014.json", "w") as f:
    json.dump(python_objects, f, indent=4)