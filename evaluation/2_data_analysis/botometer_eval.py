import csv
import botometer
from write_txt import write_txt

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


file_segment = 0
with open(f'../1_data_prep/uid_{file_segment}.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        result = bom.check_account(row[0])
        result_holder.append(result["cap"]["english"])

write_txt(f"results_{file_segment}.txt", result_holder)