# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

from google.oauth2 import service_account
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "service_account_client_secrets.json"



    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    print (credentials)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


    request = youtube.channels().list(
        part="snippet,statistics",
        id="UCq-Fj5jknLsUf-MWSy4_brA"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()


# Channels Class
class Channels:
    def __init__(self, channelid, name, subscribersCount):
        self.channelid= channelid
        self.name = name
        self.subscribersCount = subscribersCount

    def updateSubscribersCount(self,new_count):
        self.subscribersCount = new_count

# Channel Objects

tseriesObj = Channels("UCq-Fj5jknLsUf-MWSy4_brA",'T-Series',150000000)
pewObj = Channels('UC-lHJZR3Gqxm24_Vd_AJ5Yw','PewDiePie',106000000)
CocomelonObj = Channels('UCbCmjCuTUZos6Inko4u57UQ','Cocomelon - Nursery Rhymes',91200000)
setIndiaObj = Channels('UCpEhnqL0y41EpW2TvWAHD7Q','SET India',80200000)
fiveMinCraftsObj = Channels('UC295-Dw_tDNtZXFeAPAW6Aw', '5-Min Crafts',67800000)
wweObj = Channels('UCJ5v_MCY6GNUBTO8-D3XoAg', 'WWE', 64800000)
kidsDianaShowObj = Channels('UCk8GzjMOrta8yxDcKfylJYw','✿ Kids Diana Show',61500000)
zeeMusicObj = Channels('UCFFbwnve3yF62-tVXkTyHqg','Zee Music Company',60500000)
canalKondObj = Channels('UCffDXn7ycAzwL2LDlbyWOTw','Canal KondZilla',59700000)
likeNastyaObj = Channels('UCJplp5SjeGSdVdwsfb9Q7lQ','Like Nastya',59000000)
justinBeiberObj = Channels('UCIwFjwMjI0y7PDBVEO9-bkQ','Justin Bieber',56100000)

youtubeChannelsList = [tseriesObj, pewObj, CocomelonObj,setIndiaObj,fiveMinCraftsObj,wweObj,kidsDianaShowObj,zeeMusicObj,canalKondObj,likeNastyaObj,justinBeiberObj]

for i in youtubeChannelsList:
    print(youtubeChannelsList[i].name)

print(youtubeChannelsList[1].name)
