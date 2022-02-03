# This script fetches all labelled bot information and adds it to our database.
import csv
from db_connect import myscursor, mydb

p = "../../datasets/"

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


sql_insert = []

for path in paths:
    with open(p+path) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            is_bot = 0
            if(line[1] == "bot"):
                is_bot = 1
            mapVal = (line[0], is_bot)
            # print(mapVal)
            sql_insert.append(mapVal)

print(len(sql_insert))

# sql = "INSERT INTO account_status (acc_uid, is_bot) VALUES (%s, %s)"
# myscursor.executemany(sql, sql_insert)

# mydb.commit()

