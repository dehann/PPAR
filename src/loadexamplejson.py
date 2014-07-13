import json

json_data=open('example.json')

data = json.load(json_data)
json_data.close()

print "jsoned dict..."
print data["windowHeight"]
print data["plots"][1]["signals"][0]["channel"]
