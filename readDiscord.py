import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Read messages from Discord')
parser.add_argument('--channelid', dest='channelid', help='channelid') # 968749260067704856


# Main function.
def main ():

    # Parse command-line arguments
    args = parser.parse_args()
    channelid = args.channelid
    retrieve_messages('{}'.format(channelid))

def retrieve_messages(channelid):
    headers = {
        'authorization' : 'OTY4NzQ1MzcwNDA0Mzk3MDg2.YmjU-Q.QXCW2DZDyyikwJk0aacWb5Ibmm4'
    }

    r = requests.get('https://discord.com/api/v9/channels/{}/messages'.format(channelid), headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print("{}: {} \n".format(value['author']['username'], value['content']))



# Main function call.
if __name__ == '__main__':
    main()
    pass
