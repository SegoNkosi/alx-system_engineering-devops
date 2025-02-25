#!/usr/bin/python3
"""
Test the number_of_subscribers function for existing and non-existing subreddits.
"""

from number_of_subscribers import number_of_subscribers

def test_subreddits():
    existing_subreddit = "python"
    non_existing_subreddit = "nonexistingsubredditforpython"

    if number_of_subscribers(existing_subreddit) > 0:
        print("OK")
    else:
        print("Fail")

    if number_of_subscribers(non_existing_subreddit) == 0:
        print("OK")
    else:
        print("Fail")

if __name__ == "__main__":
    test_subreddits()
