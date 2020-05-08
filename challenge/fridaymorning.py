import urllib.request
import json

url= "http://api.open-notify.org/astros.json"

fileobject = urllib.request.urlopen(url)
json_text = fileobject.read()

astro = json.loads(json_text)


print("People in space: " + str(astro["number"]))
for x in astro["people"]:
    print(f"{x['name']} is on the {x['craft']}")
    #print(x["name"] + "is on the " + x["craft"])


