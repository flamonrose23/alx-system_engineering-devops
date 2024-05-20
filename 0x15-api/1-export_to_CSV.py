#!/usr/bin/python3
"""
Extending Python script by exporting data in CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for x in data2:
        if x['id'] == int(argv[1]):
            employee = x['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for x in data:

            row = []
            if x['userId'] == int(argv[1]):
                row.append(x['userId'])
                row.append(employee)
                row.append(x['completed'])
                row.append(x['title'])

                writ.writerow(row)
