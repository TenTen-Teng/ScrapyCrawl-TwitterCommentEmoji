import json
import re

origin_file = './results.json'
new_file = './newUniData.json'


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

with open(origin_file, 'r') as f:
    origin = f.readlines()

big_dict = {}
new_lines = []

for item in origin:
    new_lines.append(item)

count = 0
for item in origin:
    count += 1
    print(count)
    pair = json.loads(item, object_hook=JSONObject)
    key = pair.content + "******" + pair.title
    big_dict[key] = 0

with open(new_file, 'w') as f:
    for item in big_dict.keys():
        f.write("{\"content\": \"" + re.sub(r'\n', r'', item.split("******")[0]) + "\"," + "\"title\": \"" + re.sub(r'\n', r'', item.split("******")[1]) + "\"}\n")




