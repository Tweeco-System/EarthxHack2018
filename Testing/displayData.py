import json

file = open("FILENAME.json", "r");
for item in file:
    print(item.created_at, ' ', item.text)