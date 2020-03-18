#Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt" , headers= {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"})
text = r.text
print(text.count('a',0,len(text)))