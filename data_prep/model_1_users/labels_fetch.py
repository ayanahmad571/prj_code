# This script fetches all labelled bot information and adds it to our database.
import csv

p = "../../../datasets/"

paths = [
    "botometer-feedback-2019/botometer-feedback-2019.tsv",
    "pronbots-2019/pronbots-2019.tsv", 
    "verified-2019/verified-2019.tsv", 
    "vendor-purchased-2019/vendor-purchased-2019.tsv", 
    "political-bots-2019/political-bots-2019.tsv", 
    "celebrity-2019(1)/celebrity-2019.tsv", 
    "botwiki-2019/botwiki-2019.tsv", 
    "cresci-rtbust-2019(1)/cresci-rtbust-2019.tsv", 
    "gilani-2017/gilani-2017.tsv", 
    "midterm-2018(1)/midterm-2018.tsv"
]


sql_insert = {}

print("Fetching Labels for Data:")
for path in paths:
    print(path)
    with open(p+path) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            is_bot = 0
            if(line[1] == "bot"):
                is_bot = 1
            mapVal = {int(line[0]): is_bot}
            sql_insert.update(mapVal)
    print("Done")


