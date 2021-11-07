import os
import json

def read_json():
    path_json = '/home/rufi512/.config/qtile/settings/colors.json'
    if os.path.exists(path_json):
        try:
            file = open(path_json)
            data = json.loads(file.read())
            return data
        except:
            return '#000000'
    else:
        return '#000000'
