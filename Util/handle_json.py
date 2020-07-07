import json
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
def read_json():
    with open(base_path+"\config\data_user.json") as f:
        data = json.load(f)
    return data
def get_value(key):
    data = read_json()
    return data[key]
if __name__ == '__main__':
    print(get_value('/api3/getbanneradvertver2'))