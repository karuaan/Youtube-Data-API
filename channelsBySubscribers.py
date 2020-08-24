import os
import googleapiclient.discovery
import googleapiclient.errors
import json
import datetime

api_service_name = "youtube"
api_version = "v3"
youtube_dev_keys = 'AIzaSyAfaRcWzZheVBtQ5o1e3sudkfG9NlNF2js'

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=youtube_dev_keys)

# Channels Class
class Channels:
    def __init__(self, channelid, name):
        self.channelid= channelid
        self.name = name

# Channel Objects

tseriesObj = Channels("UCq-Fj5jknLsUf-MWSy4_brA",'T-Series')
pewObj = Channels('UC-lHJZR3Gqxm24_Vd_AJ5Yw','PewDiePie')
CocomelonObj = Channels('UCbCmjCuTUZos6Inko4u57UQ','Cocomelon - Nursery Rhymes')
setIndiaObj = Channels('UCpEhnqL0y41EpW2TvWAHD7Q','SET India')
fiveMinCraftsObj = Channels('UC295-Dw_tDNtZXFeAPAW6Aw', '5-Min Crafts')
wweObj = Channels('UCJ5v_MCY6GNUBTO8-D3XoAg', 'WWE')
kidsDianaShowObj = Channels('UCk8GzjMOrta8yxDcKfylJYw','Kids Diana Show')
zeeMusicObj = Channels('UCFFbwnve3yF62-tVXkTyHqg','Zee Music Company')
canalKondObj = Channels('UCffDXn7ycAzwL2LDlbyWOTw','Canal KondZilla')
likeNastyaObj = Channels('UCJplp5SjeGSdVdwsfb9Q7lQ','Like Nastya')
justinBeiberObj = Channels('UCIwFjwMjI0y7PDBVEO9-bkQ','Justin Bieber')

youtubechannels = [tseriesObj, pewObj, CocomelonObj,setIndiaObj,fiveMinCraftsObj,wweObj,kidsDianaShowObj,zeeMusicObj,canalKondObj,likeNastyaObj,justinBeiberObj]

# for channelObj in youtubechannels:
#    print(channelObj.channelid)

# print(youtubechannels[1].name)


# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def updateCountJob(constant_channels: list) -> list:
    channels_details: list = []
    for channelObj in constant_channels:
        
        channel_id : str = channelObj.channelid
        channel_name : str = channelObj.name
        
        print(channel_name+"\n")

        request = youtube.channels().list(
        part="statistics",
        id=channel_id,
        prettyPrint=True)

        response = request.execute()
        #new_sub_count = response["items"][0]["statistics"]["subscriberCount"]
        items: list = response.get('items')
        if (items == None):
            print ("\nItems Dictionary is not available.\n")
        else:
            statistics: list = items[0].get('statistics')   
            if (statistics == None):
                print ("\nStatistics Dictionary is not available.\n")
            else:
                sub_count: int = statistics.get('subscriberCount')
                video_count: int = statistics.get('videoCount')
                if (sub_count == None):
                    print ("\nSubscriber Count is not available!\n")
                if (video_count == None):
                    print("\nSubscriber Count is not available!\n")
                else:
                    print("Video Count: " + video_count + "\n")
                    print("Sub Count: " + sub_count + "\n")
                    stats: dict = {"Subscriber_Count" : sub_count, "Video_Count" : video_count, "Channel_ID" : channel_id}
                    channel: dict = {channel_name : stats}
                    channels_details.append(channel)
    return channels_details 
            

def make_new_file(channel_list: list) -> str:
    file_details : dict = {}
    curr_date_time : str = datetime.datetime.now().ctime()
    file_date : str = datetime.datetime.now().strftime("%A_%Y%m%d%H")
    file_name : str = file_date + ".json"
    file_path : str = "Data/" + file_name
    file_details["Title"] = "Top 10 Youtube Channels Subcribers Update"
    file_details["Last_Update_Time"] = curr_date_time
    file_details["Channel_Details"] = channel_list
    new_json_file : str = json.dumps(file_details, indent=2,sort_keys=True)
    with open(file_path,"w") as outfile:
        outfile.write(new_json_file)
    return curr_date_time

# def main():

#     api_service_name = "youtube"
#     api_version = "v3"
#     youtube_dev_keys = 'AIzaSyAfaRcWzZheVBtQ5o1e3sudkfG9NlNF2js'

#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, developerKey=youtube_dev_keys)


#     request = youtube.channels().list(
#         part="snippet,statistics",
#         id="UCq-Fj5jknLsUf-MWSy4_brA"
#     )
#     response = request.execute()

#     reponse_type = type(response)

#     print(reponse_type)

#     json_formatted_string = json.dumps(response, indent=2)

#     print(json_formatted_string)

if __name__ == "__main__":
    channel_details : list = updateCountJob(youtubechannels)
    make_new_file(channel_details)