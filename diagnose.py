import json

def get_data(tag):
    with open('tags.json') as jsonfile:
        labels = json.load(jsonfile)
        for label in labels['conditions']:
            if tag == label['tag']:
                return label

    return 0



