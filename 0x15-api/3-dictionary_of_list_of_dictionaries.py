#!/usr/bin/python3
"""
Extending Python script by exporting data in JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    nw_dict1 = {}

    for y in data2:

        row = []
        for x in data:

            nw_dict2 = {}

            if y['id'] == x['userId']:

                nw_dict2['username'] = y['username']
                nw_dict2['task'] = x['title']
                nw_dict2['completed'] = x['completed']
                row.append(nw_dict2)

        nw_dict1[y['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(nw_dict1)
        f.write(json_obj)
