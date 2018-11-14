#! python3
# mapIt.py - Launches a map i the browser using an address from the command line or clipboard
"""
This is a little python widget to help window users to use Google maps via Command Prompt. Type in the name of the address
after properly setting up the environment variables.

Vincent Huang

"""

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
