import sys
import clipboard
import json
import uuid

def save():

    clipboard_data = clipboard.paste()
    key = input("Enter a name for the data: ")
    clipboard_dict = {key: clipboard_data}
    new_id = str(uuid.uuid4())
    initial_dict = {}

    with open("clipboard.json", "r") as f:
        try:
            current_data = json.load(f)
        except:
            current_data = None

    if current_data == None:
        initial_dict[new_id] = clipboard_dict
        with open("clipboard.json", "w") as f:
            json.dump(initial_dict, f)

    else:
        current_data[new_id] = clipboard_dict
        with open("clipboard.json", "w") as f:
            json.dump(current_data, f)

    print(clipboard_data, " saved as ", key)

def get():
    print("get")

def remove():
    print("remove")


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