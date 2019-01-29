import requests
import json

baseURL = 'https://discordapp.com/api/v6/'
serverID = ''

authString = ''

r = requests.get(baseURL+'/channels/'+serverID+'/messages', headers={'Authorization': 'Bot ' + authString})


snowflakes = []
for item in r.json():
    snowflakes.append(item['id'])

if 2 < len(snowflakes) < 100:

    r = requests.post(baseURL+'/channels/'+serverID+'/messages/bulk-delete',
        headers={'Authorization': 'Bot ' + authString, 'Content-Type': 'application/json', 'Accept': 'application/json'},
        data=json.dumps({'messages': snowflakes}))

elif len(snowflakes) > 100:
    while len(snowflakes) > 100:
        snowflakes.pop(0)

    r = requests.post(baseURL + '/channels/' + serverID + '/messages/bulk-delete',
        headers={'Authorization': 'Bot ' + authString, 'Content-Type': 'application/json', 'Accept': 'application/json'},
        data=json.dumps({'messages': snowflakes}))
