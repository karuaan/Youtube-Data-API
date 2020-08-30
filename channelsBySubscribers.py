import os
import googleapiclient.discovery
import googleapiclient.errors
import json
import datetime
from collections import OrderedDict
import time
import boto3
from botocore.exceptions import NoCredentialsError

api_service_name = "youtube"
api_version = "v3"
youtube_dev_keys = 'AIzaSyAfaRcWzZheVBtQ5o1e3sudkfG9NlNF2js'

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=youtube_dev_keys)

AWS_ACCESS_KEY_ID = 'AKIAJ4HQ5WOTNEFOBF7A'
AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'youtubechannelsdatas3'

def upload_to_s3(data: str, bucket: str, s3_file: str):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    try:
        s3.put_object(Body=data, Bucket=bucket, Key=s3_file)
        print("Upload Successful")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False

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
        
        channel_id: str = channelObj.channelid
        channel_name: str = channelObj.name
        
        print(channel_name+"\n")

        request = youtube.channels().list(
        part="statistics,contentDetails",
        id=channel_id,
        prettyPrint=True)

        response = request.execute()
        items: list = response.get('items')
        if (items == None):
            print ("\nItems Dictionary is not available.\n")
        else:
            statistics: list = items[0].get('statistics')   
            content_details: list = items[0].get('contentDetails')
            if (content_details == None):
                print ("\nContent Details Dictionary is not available.\n")
            else:
                relatedPlaylists: dict = content_details.get('relatedPlaylists')
                if (relatedPlaylists == None):
                    print ("\Related Playlists Dictionary is not available.\n")
                else:
                    uploads: str = relatedPlaylists.get('uploads')
                    if (uploads == None):
                        print ("\nUploads ID is not available.\n")
                    else:
                        print ("Uploads ID:" + uploads)
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
                stats: dict = {"Subscriber_Count" : sub_count, "Video_Count" : video_count, "Channel_ID" : channel_id, "Uploads ID" : uploads}
                channel: dict = {"Name" : channel_name, "Details" : stats}
                channels_details.append(channel)
    return channels_details 

def make_new_file(channel_list: list) -> list:
    file_details: dict = {}
    curr_date_time: str = datetime.datetime.now().ctime()
    file_year: str = datetime.datetime.now().strftime("%Y")
    file_month: str = datetime.datetime.now().strftime("%m")
    file_day: str = datetime.datetime.now().strftime("%d")
    file_hour: str = datetime.datetime.now().strftime("%H")
    file_name: str = "channel_details.json"
    file_path: str =  file_year + "/" + file_month + "/" + file_day + "/" + file_hour + "/" + file_name
    file_details["Title"] = "Top 10 Youtube Channels Subcribers Update"
    file_details["Last_Update_Time"] = curr_date_time
    file_details["Channel_Details"] = channel_list
    new_json_file: str = json.dumps(file_details, indent=2)
    upload_to_s3(new_json_file, bucket_name, file_path)
    return [curr_date_time, file_path]

def make_latest_file(channel_list: list) -> list:
     file_details: dict = {}
     curr_date_time: str = datetime.datetime.now().ctime()
     file_name: str = "latest.json"
     file_details["Title"] = "Top 10 Youtube Channels Subcribers Update"
     file_details["Last_Update_Time"] = curr_date_time
     file_details["Channel_Details"] = channel_list
     new_json_file: str = json.dumps(file_details, indent=2)
     upload_to_s3(new_json_file,bucket_name,file_name)

# def find_latest_videos(playlist_id: str, num_of_new_videos: int) -> dict:
#     latest_videos: dict = {}
#     request = youtube.channels().list(
#         part="contentDetails,snippet",
#         maxResults=num_of_new_videos,
#         playlistId=playlist_id,
#         prettyPrint=True
#     )
#     response = request.execute()
#     videos: list = response.get("items")
#     if (videos == None):
#         print ("\nVideos List is not available.\n")
#     else:
#         new_vids: list = []
#         for video in videos:
#             content_details = video.get("contentDetails")
#             if (content_details == None):
#                 print("\nContent Details Dictionary does not exist!\n")
#             else:
#                 video_id = video.get("videoId")
#                 new_vids.append(video_id)
#     latest_videos = {"Name" : name,"New Videos" : new_vids}
#     return latest_videos

def get_channel_playlist_id(channel_name: str) -> str:
    with open("Data/latest.json") as file:
        channel_details: list = file.get("Channel_Details")
        if (channel_details == None):
            print("\nChannel Details List does not exist!\n")
        else:
            for channel in channel_details:
                channel_title = channel.get("Name")
                if (channel_title == None):
                    print("\nChannel Name does not exist!\n")
                elif (channel_title == channel_name):
                    details: dict = channel.get("Details")
                    if (details == None):
                        print("\nChannel Details do not exist!\n")
                    else:
                        playlist: str = details.get("Uploads ID")
                        if (playlist == None):
                            print("\nPlaylist ID does not exist for this channel!\n")
                        else:
                            return playlist
                else:
                    continue

def get_sub_count(channel_name: str, file: str) -> int:
    with open(file) as f:
        channel_details: list = f.get("Channel_Details")
        if (channel_details == None):
            print("\nChannel Details List does not exist!\n")
        else:
            for channel in channel_details:
                channel_title = channel.get("Name")
                if (channel_title == None):
                    print("\nChannel Name does not exist!\n")
                elif (channel_title == channel_name):
                    details: dict = channel.get("Details")
                    if (details == None):
                        print("\nChannel Details do not exist!\n")
                    else:
                        sub_count = details.get("Subscriber_Count")
                        if (sub_count == None):
                            print("\nNo Videos Exist!\n")
                        else:
                            return int(sub_count)
                else:
                    continue

def channel_video_count_finder(channel_name: str, file: str) -> int:
    with open(file) as f:
        channel_details: list = f.get("Channel_Details")
        if (channel_details == None):
            print("\nChannel Details List does not exist!\n")
        else:
            for channel in channel_details:
                channel_title = channel.get("Name")
                if (channel_title == None):
                    print("\nChannel Name does not exist!\n")
                elif (channel_title == channel_name):
                    details: dict = channel.get("Details")
                    if (details == None):
                        print("\nChannel Details do not exist!\n")
                    else:
                        video_count = details.get("Video_Count")
                        if (video_count == None):
                            print("\nNo Videos Exist!\n")
                        else:
                            return int(video_count)
                else:
                    continue

def runScript():
    channel_details: list = updateCountJob(youtubechannels)
    new_file_details = make_new_file(channel_details)
    run_time = new_file_details[0]
    new_file = new_file_details[1]
    make_latest_file(channel_details)
    print ("\n" + run_time + " run is completed!")

def lambda_handler(event, context):
    try:
        print("Writing Data to S3 Bucket!")
        runScript()
        print("Data Write is completed ")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    runScript()