import urllib3
import requests 

url = "https://raw.githubusercontent.com/echen102/"

months_2020 = ["2020-08","2020-09","2020-10","2020-11","2020-12", "2021-01","2021-02","2021-03","2021-04"]
intervals = {1,3}
file_names = list()
for m in months_2020:
    print(m,"_________")
    for d in range(31):
        new_d = d + 1
        for t in intervals:
            padded_d = new_d
            if len(str(new_d)) < 2:
                padded_d = f"0{new_d}"
            file_name = f'us-pres-elections-2020/master/{m}/us-presidential-tweet-id-{m}-{padded_d}-0{t}.txt'
            file_names.append(file_name)
        

# for f in file_names:

#     total_url = f"{url}{f}"
#     file_name = total_url.split('/')[-1]
#     x = requests.get(total_url, auth=('ayanahmad5701@gmail.com', 'AAhmad2001.'))

#     if x.status_code == 200:

#         f = open(file_name, 'wb')
#         buffer = x.content
#         f.write(buffer)
#         f.close()
#     else:
#         print("Not Found: ", total_url)