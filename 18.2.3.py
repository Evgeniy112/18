import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)
p = str(r[0])
myText = open("my_texts.txt", "w", encoding="utf8")
myText.write(p)
myText.close()
