#Create a new endpoint 
import json
import requests
url = "https://ise.devnetsandbox.com/ers/config/endpoint"
payload = {
    "ERSEndpoint": {
        "name": "Devnet Endpoint-1",
        "description": "DevNet Endpoint-1",
        "mac" : "FF:EE:DD:03:04:05",
        "groupId" : " 00000000-1111-2222-3333-444444444444",
        "staticGroupAssignment": True

    }
}

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'authorization': "Basic ZGV2YXNjOnN0cm9uZ3Bhc3N3b3JkJw==",
    'cache-control': "no-cache",
}


response = requests.request(
    "POST",
    url,
    data=json.dumps(payload),
    headers=headers

)
print (response.text)