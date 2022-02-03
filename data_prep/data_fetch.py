import json

p = "../../datasets/"

paths = [
    "botometer-feedback-2019/botometer-feedback-2019_tweets.json",
    "pronbots-2019/pronbots-2019.json", 
    "verified-2019/verified-2019.json", 
    "vendor-purchased-2019/vendor-purchased-2019.json", 
    "political-bots-2019/political-bots-2019.json", 
    "celebrity-2019(1)/celebrity-2019.json", 
    "botwiki-2019/botwiki-2019.json", 
    "cresci-rtbust-2019(1)/cresci-rtbust-2019.json", 
    "gilani-2017/gilani-2017.json", 
    "midterm-2018(1)/midterm-2018.json"
]

# Opening JSON file
f = open(p+paths[0])
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
print(data)
 
# Closing file
f.close()