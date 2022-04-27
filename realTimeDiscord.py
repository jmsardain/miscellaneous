import websocket
import json
import threading
import time
import ssl
import argparse

parser = argparse.ArgumentParser(description='Read messages from Discord in real time')
parser.add_argument('--token', dest='token', help='token') # OTY4NzQ1MzcwNDA0Mzk3MDg2.YmjU-Q.QXCW2DZDyyikwJk0aacWb5Ibmm4


# Main function.
def main ():

    # Parse command-line arguments
    args = parser.parse_args()
    token = args.token

    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    event = receive_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

    token = "{}".format(token)
    payload = {
        'op': 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "macOS",
                "$browser": "Safari",
                "$device": 'pc'
            }
        }
    }

    send_json_request(ws, payload)

    while True:
        event = receive_json_response(ws)
        try:
            print("{}: {}".format(event['d']['author']['username'], event['d']['content']))
            op_code = event('op')
            if op_code == 11:
                print('heartbeat received')
        except:
            pass

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("Heartbeat sent")


# Main function call.
if __name__ == '__main__':
    main()
    pass
