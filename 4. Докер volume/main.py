import os
import json

FILE_PATH = 'file.json'

if os.path.exists(FILE_PATH):
    print(f'Append to {os.path.abspath(FILE_PATH)}')

    with open(FILE_PATH, 'r') as file:
        data = json.load(file)

    last_launch = max(map(lambda d: d['launchNumber'], data))
    data.append({ 'launchNumber': last_launch + 1 })

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f'Create file {os.path.abspath(FILE_PATH)}')

    with open(FILE_PATH, 'w') as file:
        json.dump([{ 'launchNumber': 1 }], file, indent=4)
