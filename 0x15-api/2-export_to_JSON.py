#!/usr/bin/python3
"""
Extending Python script by exporting data in JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for x in data2:
        if x['id'] == int(argv[1]):
            u_name = x['username']
            id_no = x['id']

    row = []

    for x in data:

        nw_dict = {}

        if x['userId'] == int(argv[1]):
            nw_dict['username'] = u_name
            nw_dict['task'] = x['title']
            nw_dict['completed'] = x['completed']
            row.append(nw_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
