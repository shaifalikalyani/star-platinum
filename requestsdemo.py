import requests

r = requests.get('https://api.github.com/events', verify=False)
r.text