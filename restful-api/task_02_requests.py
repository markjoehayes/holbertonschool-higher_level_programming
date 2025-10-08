#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONplaceholder and prints the status code and title"""
    # Fetch posts from JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # print the status code
    print(f"Status Code: {response.status_code}")
    # If request was successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()
        # iterate through posts and print titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves them to a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # if request was successful, process and save data
    if response.status_code == 200:
        posts = response.json()
        # structure data into a list of dicts with only id, title and body
        structured_posts = [
                {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                 }
                 for post in posts 
        ]

        # wrire to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts saved to posts.csv")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
