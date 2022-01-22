import requests
import os
import random
import sys
import urllib3
import string
import json
from discord_webhook import DiscordWebhook

count = 0


print(sys.version)

def create_str(str_length):
    return random.sample(string.ascii_letters, str_length)

def create_num(num_length):
    digits = []
    for i in range(num_length):
        digits.append(str(random.randint(1, 100)))

    return digits

def create_special_chars(special_length):
    stringSpecial = []
    for i in range(special_length):
        stringSpecial.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))

    return stringSpecial


str_cnt = (random.randint(1,10))

num_cnt = (random.randint(1,10))

password_values = create_str(int(str_cnt)) +create_num(int(num_cnt))

#shuffle/mix the values
random.shuffle(password_values)
content = (''.join(password_values))

url = "https://discord.com/api/webhooks/934147191054954537/wApgqQ7iG-3kLZgc0g-OHxinzaYxIFvE5gyl7lTRgCVS1rIhxFO2EK8ReM6t6GapP7PP"



proxies = {
  'http': 'http://167.172.203.244:8118',
  'http': 'http://144.202.113.90:8080',
  'http': 'http://147.135.255.62:8122',
  'http': 'http://147.135.255.62:8242',
  'http': 'http://167.172.203.244:8118',
  'http': 'http://66.170.183.90:9090',
  'http': 'http://43.249.224.170:82',
  'http': 'http://144.202.113.90:8080',
  'http': 'http://147.135.255.62:8122',
 # 'https': 'http://88.157.181.42:8080',
#  'https': 'http://209.140.194.152:3128',
#  'https': 'http://165.22.59.84:8080',
#  'https': 'http://147.135.255.62:8139',
#  'https': 'http://147.135.255.62:8256',
  
  
}

webhook = DiscordWebhook(url=url, content=content, proxies=proxies)


while True:
    responce = webhook.execute()
    count = count+1
    print("[+] Sent " + str(count))
    


