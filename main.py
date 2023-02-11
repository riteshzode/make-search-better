import webbrowser
import sys


def create_filter():
    valid_website = ['reddit.com', 'stackoverflow.com', 'stackexchange.com', 'medium.com']

    filters = " ("

    for index, website in enumerate(valid_website):
        filters += 'site:' + website
        if index == len(valid_website) - 1:
            filters += ')'
        else:
            filters += ' OR '

    return filters


def create_query():
    return "https://www.google.com/search?q=" + " ".join(sys.argv[1:]) + create_filter()


def open_chrome():
    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if len(sys.argv[1:]) == 0:
        print(f"Error: please enter a valid search query")
    else:
        webbrowser.get(chrome_path).open(create_query())


open_chrome()
