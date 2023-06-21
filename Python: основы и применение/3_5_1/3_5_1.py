import requests
import json
nums = []
with open('dataset_24476_3.txt','r') as ds:
    for line in ds:
        nums.append(int(line))
with open ('result.txt', 'w') as res:
    for i in nums:
        url = f'http://numbersapi.com/{i}/math?json=true'
        data = (requests.get(url)).json()
        if data['found'] == True:
            res.write('Interesting\n')
        else:
            res.write('Boring\n')

