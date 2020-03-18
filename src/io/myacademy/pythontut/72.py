#Create a script that takes a user input and opens browser and searches that text on google

import webbrowser

word = input("Enter the text to search")
webbrowser.Chrome.open_new_tab(webbrowser, url="https://www.google.com/search?q=" + word)
