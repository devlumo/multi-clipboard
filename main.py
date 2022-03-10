from pickle import FALSE
import sys
import clipboard
import json
import uuid
from os.path import exists

filename = "clipboard.json"

def save():

    new_id = str(uuid.uuid4())
    key = input("Enter a name for the data: ").upper()

    # check if the name provided is already in the file, in that case we need a different one
    value = search_file(key, "g")
    if value:
        while(value):
            print(key, "already exists")
            key = input("Enter a different name for the data: ").upper()
            value = search_file(key, "g")

    clipboard_data = clipboard.paste()
    clipboard_dict = {key: clipboard_data}
    initial_dict = {}

    # create file if it doesn't exist
    if not exists(filename):
        open(filename, 'w').close()

    # check if there is anything in the file, if there is take the data and convert to dict
    with open(filename, "r") as f:
        try:
            current_data = json.load(f)
        except:
            current_data = None

    # if not create new json object in the file
    if current_data == None:
        initial_dict[new_id] = clipboard_dict
        with open(filename, "w") as f:
            json.dump(initial_dict, f)

    # append new data to dict and add to the file
    else:
        current_data[new_id] = clipboard_dict
        with open(filename, "w") as f:
            json.dump(current_data, f)

    print(clipboard_data, "saved as", key)

def search_file(search_key, command):
    if not exists(filename):
        print("Theres nothing in the clipboard")
        return None

    with open(filename, "r") as f:
        try:
            current_data = json.load(f)
        except:
            current_data = None

    if not current_data:
        print("Theres nothing in the clipboard")
        return None
    else:
        for i, key in enumerate(current_data):
            result = None
    
            if search_key in current_data[key]:
                if command == "g":
                    result = current_data[key]
                else:
                    result = key, current_data
                break

        return result

def get():

    key = input("Enter the key: ").upper()
    value = search_file(key, "g")

    if not value:
        print("Couldn't find ", key)
    else:
        copy_value = value.get(key)
        clipboard.copy(copy_value);
        print(key, "copied!")

def remove():
    key = input("Enter the key: ").upper()
    value = search_file(key, "d")

    if not value:
        print("Couldn't find ", key)
    else:
        key_to_delete = value[0]
        data = value[1]
        
        del data[key_to_delete]

        with open(filename, "w") as f:
            json.dump(data, f)
        
        print(key, "removed")


if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "save":
        save()
    elif command == "get":
        get()
    elif command == "remove":
        remove()
    else:
        print("Error: Incorrect argument provided - avaliable args: save, get, remove")
else:
    print("Please only provide only one argument - save, get, remove")