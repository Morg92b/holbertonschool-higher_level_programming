#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for index in posts:
            print(index['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ['id', 'title', 'body']
            writer.writerow(fields)
            for index_2 in posts:
                writer.writerow([index_2['id'], index_2['title'],
                                 index_2['body']])
