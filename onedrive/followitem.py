import sys
import json
import logging

import requests
import msal

from azure.identity import DeviceCodeCredential, ClientSecretCredential
from msgraph.core import GraphClient

this = sys.modules[__name__]

config = json.load(open(sys.argv[1]))

# create app instance TODO maintian token
app = msal.ConfidentialClientApplication(
    config["client_id"], 
    authority=config["authority"],
    client_credential=config["secret"],
    # TODO Token cache
)

# pattern to acquire token
result = None

# look up token from cache
# looking for token for current app - not end user
result = app.acquire_token_silent(config["scope"], account=None)

if not result:
    print("No suitable token exists in cache. Getting new token.")
    result = app.acquire_token_for_client(scopes=config["scope"])

# if "access_token" in result:
#     graph_data = requests.get(
#         config["endpoint"],
#         headers={'Authorization': 'Bearer ' + result['access_token']}, ).json()
#     print("Graph API result: ")
#     print(json.dumps(graph_data, indent=2))
# else:
#     print(result.get("error"))
#     print(result.get("error_description"))
#     print(result.get("correlation_id"))


def initialiseGraph():
    # this.app_client = ClientSecretCredential(config["tenant_id"],config["client_id"],config["secret"])

    this.user = app.acquire_token_on_behalf_of(result["access_token"], config["scope"])
    print(this.user)
    # access_token = this.app_client.get_token(config["scope"])
    # print("Token : " + access_token.token)
    # this.user_client = GraphClient(credenital=this.app_client, scopes=config["scope"])
    # url = f'{config["endpoint"]}?$select={"displayName,mail,userPrincipalName"}'
    # user_client.get(url)

def getUser():
    if "access_token" in result:
        graph_data = requests.get(
            config["endpoint"] + "/users",
            headers={'Authorization': 'Bearer ' + result['access_token']}, 
        ).json()

        # print("Graph API result: ")
        # print(json.dumps(graph_data, indent=2))
        return graph_data
    else:
        print(result.get("error"))
        print(result.get("error_description"))

def makeAPICall(userId):
    data = requests.get(
        # config["endpoint"] + "/drives",
        config["endpoint"] + "/users/" + userId + "/drive/items",
        headers={'Authorization': 'Bearer ' + result['access_token']}, 
        ).json()
    print(json.dumps(data, indent=2))
  

def getOneDriveItems():
    if "access_token" in result:
        graph_data = requests.get(
            config["endpoint"] + "/me/drive/root/children",
            headers={'Authorization': 'Bearer ' + result['access_token']}, ).json()
        print("Result: ")
        print(json.dumps(graph_data, indent=2))
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))

if __name__=='__main__':
    initialiseGraph()
    # print(result)
    # user = getUser()
    # id = user["value"][0]["id"]
    # print("\nUser Id: ")
    # print(id)
    # makeAPICall(id)
    # getOneDriveItems()
    print()
