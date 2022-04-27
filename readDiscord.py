import requests
import json

def retrieve_messages(channelid):
    headers = {
        'authorization' : 'OTY4NzQ1MzcwNDA0Mzk3MDg2.YmjU-Q.QXCW2DZDyyikwJk0aacWb5Ibmm4'
    }

    r = requests.get('https://discord.com/api/v9/channels/{}/messages'.format(channelid), headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print("{}: {} \n".format(value['author']['username'], value['content']))

retrieve_messages('968749260067704856')
