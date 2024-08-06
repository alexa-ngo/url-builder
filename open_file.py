import sys
import os
import json
from url_lib.url_builder import dict_to_str

# This open_file.py reads the input file and returns a formatted URL.
# Example in terminal: $python3 open_file.py file.json

# If there is not a file, exit the python program.
if len(sys.argv) <= 1:
    print("Please provide a filename.")
    exit()

# Opens a JSON file and prints the requested URL.
file_path = sys.argv[1]

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as read_file:
        input_dict = json.load(read_file)
        print(dict_to_str(input_dict))

else:
    print('the specified file does NOT exist!')




