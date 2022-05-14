import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

wordlist = open('wordlist.txt')

args = sys.argv[1:]
if not args:
    print("Usage: python3 my_finder.py IP")
    print("Example Of Usage: python3 my_finder.py 10.11.100.125")
    exit()

word = wordlist.readline()
while word:
    URL = "https://"+args[0]+"/"+word.strip()
    r = requests.get(url = URL, verify=False)
    if (r.status_code != 404):
        print(URL+": "+str(r.status_code))
    word = wordlist.readline()

wordlist.close()
