import os 
import json
import urllib

print("Hello from the script")
def readJson(path) :
  with open(path) as json_file:
    data = json.load(json_file)
    return data
print(os.environ['PATH'])
for f in os.listdir("."):
  print(f)
path = os.environ['GITHUB_EVENT_PATH']
print('Event path is %s' % path)
event = readJson(path)
print(json.dumps(event,indent=2))
url = event['head_commit']['url']
print('HEAD is at %s' % url)
