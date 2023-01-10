import os
import json
home = os.getenv('HOME', default='')
def read_json():
    path_json = home + '/.config/qtile/settings/colors.json'
    if os.path.exists(path_json):
        try:
            file = open(path_json)
            data = json.loads(file.read())
            return data
        except:
            return '#000000'
    else:
        return '#000000'
