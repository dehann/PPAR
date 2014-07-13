import json

json_data=open('../data/example.json')

data = json.load(json_data)
json_data.close()

print "jsoned dict..."
print data["windowHeight"]
print data["plots"][1]["signals"][0]["channel"]
reqstr = "[\"plots\"][1][\"signals\"][0][\"channel\"]"
print eval("data" + reqstr)

