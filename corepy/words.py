
#! python
"""Retrive and print words from a URL

Usage:
   
   Additional help:

   To reload the updated file from REPL
   import importlib
   importlib.reload(words)

    python words.py <URL.

    To call this from REPL (Powershell) use as below
    import words
    from words import *
     main("http://sixty-north.com/c/t.txt")
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
       
       Args:
           url: The URL of UTF-8 text document.

        Returns:
           A List of strings containing the words from
           the document.
    """
    story = urlopen(url)
    story_words=[]
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(items):
    """Print items one per line.
    
       Args:
           An iterable series of printable items.
    """
    for item in items:
        print(item)


#Called as dunder name if prefix and suffix have "__"
def main(url):
    """Print each word from a text document from at a URL.

       Args:
           url: The URL of a UTF-8 text document.
           Example: main("http://sixty-north.com/c/t.txt")
     """
    words = fetch_words(url)
    print_words(words)

 
if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename.