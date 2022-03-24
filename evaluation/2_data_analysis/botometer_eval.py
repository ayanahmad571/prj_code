import csv
import botometer
from write_txt import write_txt
import tweepy

rapidapi_key = "e2f76211acmshe44706172ba098fp120825jsn767145c88be8"
twitter_app_auth = {
    'consumer_key': 'J7mRRswtZwKMMi6gBjr5yPg6d',
    'consumer_secret': 'LxUEu6dLRkS96q4rbwNcVEwOyw6LCERUS9ZM3YwMABY7edJZ6Q',
    'access_token': '1092080822822322176-1H31LuOQ9Wa3otSKSueCKxane8TL1k',
    'access_token_secret': 'EzrgDuLAld5haBvo9bainNtlRmPKeC49A7dN8MIoAUAsQ',
}
bom = botometer.Botometer( wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


result_holder = list()


file_segment = 1
with open(f'../1_data_prep/uid_{file_segment}.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        try:
            result = bom.check_account(row[0])
            print(row[0],":",result["cap"]["english"])
            result_holder.append(result["cap"]["english"])
        except tweepy.error.TweepError:
            print(f"Oops! {row[0]} cant be worked")
        

write_txt(f"results_{file_segment}.txt", result_holder)