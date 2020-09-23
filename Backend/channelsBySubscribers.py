import os
import googleapiclient.discovery
import googleapiclient.errors
import json
import datetime
from collections import OrderedDict
import time
import boto3
from botocore.exceptions import NoCredentialsError
from Data.Channels_Data import youtubechannels
from Keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, youtube_dev_keys

api_service_name = "youtube"
api_version = "v3"
#youtube_dev_keys = 'AIzaSyAfaRcWzZheVBtQ5o1e3sudkfG9NlNF2js'

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=youtube_dev_keys)

# AWS_ACCESS_KEY_ID = 'AKIAIKWAPGO3XRCZZM5A'
# AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'youtubechannelsdatas3'

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def upload_to_s3(data: str, bucket: str, s3_file: str):
    try:
        s3.put_object(Body=data, Bucket=bucket, Key=s3_file)
        print("\nUpload Successful\n")
        return True
    except NoCredentialsError:
        print("\nCredentials not available\n")
        return False

# Channels Class
class Channels:
    def __init__(self, channelid, name):
        self.channelid= channelid
        self.name = name

# # Channel Objects

tseriesObj = Channels("UCq-Fj5jknLsUf-MWSy4_brA",'T-Series')
pewObj = Channels('UC-lHJZR3Gqxm24_Vd_AJ5Yw','PewDiePie')
CocomelonObj = Channels('UCbCmjCuTUZos6Inko4u57UQ','Cocomelon - Nursery Rhymes')
fiveMinCraftsObj = Channels('UC295-Dw_tDNtZXFeAPAW6Aw', '5-Min Crafts')
setIndiaObj = Channels('UCpEhnqL0y41EpW2TvWAHD7Q','SET India')
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

def sort_videos_list_dict(videos_list: list) -> list:
    temp: list = []
    for video in videos_list:
        video_details: dict = video.get("Video_Details")
        if (video_details == None):
            print("\nVideo Details are not available.\n")
        else:
            video_score: int = video_details.get("Video_Score")
            if (video_score == None):
                print("\nVideo Score is not available.\n")
            else:
                temp.append(video_score)
                continue

    temp_len: int = len(temp)
    for val in range(1,temp_len):
        insert_item: int = temp[val]
        insert_dict: dict = videos_list[val]
        j = val-1

        while j >= 0 and temp[j] < insert_item:
            videos_list[j + 1] = videos_list[j]
            temp[j + 1] = temp[j]
            j-=1

            videos_list[j + 1] = insert_dict
            temp[j + 1] = insert_item
    return videos_list

def sort_channels_list_by_Subs(channels_list: list) -> list:
    temp: list = []
    for channel in channels_list:
        channel_details: dict = channel.get("Details")
        if (channel_details == None):
            print("\nChannel Details are not available.\n")
        else:
            sub_count: int = int(channel_details.get("Subscriber_Count"))
            if (sub_count == None):
                print("\nSub Count is not available.\n")
            else:
                temp.append(sub_count)
                continue

    temp_len: int = len(temp)
    for val in range(1,temp_len):
        insert_item: int = temp[val]
        insert_dict: dict = channels_list[val]
        j = val-1

        while j >= 0 and temp[j] < insert_item:
            channels_list[j + 1] = channels_list[j]
            temp[j + 1] = temp[j]
            j-=1

            channels_list[j + 1] = insert_dict
            temp[j + 1] = insert_item
    return channels_list

def get_playlist_items(playlist_id: str, num_of_new_videos: int) -> list:
    videos: list = []
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=num_of_new_videos,
        playlistId=playlist_id,
        prettyPrint=True
    )
    response = request.execute()

    items: list = response.get("items")
    if (items == None):
        print("\nItems List does not exist.\n")
    else:
        for video in items:
            video_details: dict = video.get("snippet")
            if (video_details == None):
                print("\nVideo Details Do not exist.\n")
            else:
                resource: dict = video_details.get("resourceId")
                if (resource == None):
                    print("\nVideo Resource does not exist.\n")
                else:
                    video_id: str = resource.get("videoId")
                    if (video_id == None):
                        print("\nVideo ID does not exist.\n")
                    else:
                        video_details: dict = get_video_details(video_id)
                        temp: dict = { "Video_ID" : video_id, "Video_Details" :  video_details}
                        videos.append(temp)
        return videos

def get_video_details(video_id: str) -> list:
    
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    response = request.execute()
    items: list = response.get("items")
    if (items == None):
        print("\nItems List does not exist.\n")
    else:
        video: dict = items[0]
        snippet: dict = video.get("snippet")
        if (snippet == None):
            print("\nSnippet Dictionary is not available.\n")
        else:
            published_time: str = snippet.get("publishedAt")
            video_title: str = snippet.get("title")
            video_description: str = snippet.get("description")
            if (video_description == None):
                print("\nVideo Description for " + video_id + " is not available.\n")
            if (video_title == None):
                print("\nVideo Title for " + video_id + " is not available.\n")
            if (published_time == None):
                print("\nPublished Time is not available.\n")
            else:
                statistics: dict = video.get("statistics")
                # print("")
                # print(statistics)
                # print("")
                if (statistics == None):
                    print("\nStatistics Dictionary is not available.\n")
                else:
                    view_count: str = statistics.get("viewCount")
                    like_count: str = statistics.get("likeCount")
                    dislike_count: str = statistics.get("dislikeCount")
                    comment_count: str = statistics.get("commentCount")
                    print(" ")
                    print(video_id)
                    print(" ")
                    print(comment_count)
                    print(" ")
                    if (view_count == None):
                        print("\nView Count for "+ video_id + " is not available.\n")
                        view_count = 0
                    if (like_count == None):
                        print("\nLike Count for "+ video_id + " is not available.\n")
                        like_count = 0
                    if (dislike_count == None):
                        print("\nDislike Count for "+ video_id + " is not available.\n")
                        dislike_count = 0
                    if (comment_count == None):
                        print("\nComments Count for "+ video_id + " is not available.\n")
                        comment_count = 0

                    video_score: int = judge_popular_video_score(like_count, dislike_count, view_count, comment_count, published_time)

                    video_details: dict = {"Title" : video_title, "Published_Time" : published_time, "Video_Description" : video_description, "View_Count" : view_count, "Like_Count" : like_count, "Dislike_Count" : dislike_count, "Comment_Count" : comment_count, "Video_Score" : video_score}
        return video_details

def judge_popular_video_score(like_count: str, dislike_count: str, view_count: str, comments_count: str, published_time: str) -> int:
    curr_time = datetime.datetime.utcnow()
    published_datetime = datetime.datetime.strptime(published_time,"%Y-%m-%dT%H:%M:%SZ") # 2020-09-07T16:15:03Z
    time_change = curr_time - published_datetime
    total_seconds = time_change.total_seconds()
    minutes_passed = total_seconds//60
    if (minutes_passed == 0):
        minutes_passed = 100000000000
    total_votes: int = int(like_count) + int(dislike_count)
    if (total_votes == 0):
        total_votes = 100000000000
    positive_ratio: float = int(like_count)/total_votes

    total_contribution = int(view_count) + int(comments_count)

    positive_score: int = (total_contribution * positive_ratio)//minutes_passed 
    return positive_score

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
            statistics = items[0].get('statistics')
            content_details = items[0].get('contentDetails')
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
                    print("Video Count: " + str(video_count) + "\n")
                    print("Sub Count: " + str(sub_count) + "\n")
                stats: dict = {"Subscriber_Count" : sub_count, "Video_Count" : video_count, "Channel_ID" : channel_id, "Uploads ID" : uploads}
                channel: dict = {"Name" : channel_name, "Details" : stats}
                channels_details.append(channel)
    return channels_details 
     
def read_latest_file() -> dict:
    try:
        print("\nFile Read is in progress!\n")
        data = s3.get_object(Bucket=bucket_name, Key='latest.json')
        body: str = data['Body'].read()
        contents: dict = json.loads(body)
        return contents
    except NoCredentialsError:
        print("Credentials not available")
        return {}

def get_new_channel_details(channel_name: str, new_channel_details: list) -> list:
    new_details = []
    for channel in new_channel_details:
        name: str = channel.get('Name')
        if (name == None):
            print ("\nChannel Names are not available.\n")
        else:
            if (name == channel_name):
                channel_details: dict =  channel.get('Details')
                if (channel_details == None):
                    print ("\nChannel Details for " + name +  " are not available.\n")
                else:
                    sub_count = channel_details.get('Subscriber_Count')
                    video_count = channel_details.get('Video_Count')
                    playlist_id = channel_details.get('Uploads ID')
                    if (sub_count == None):
                        print ("\nChannel " + name + " subscriber count is not available.\n")
                    else:
                        new_details.insert(0,sub_count)
                    if (video_count == None):
                        print ("\nChannel " + name + " video count is not available.\n")
                    else:
                        new_details.insert(1,video_count)
                    if (playlist_id == None):
                        print ("\nChannel " + name + " playlist id is not available.\n")
                    else:
                        new_details.insert(2,playlist_id)
                return new_details
            else:
                continue
            
def get_old_channel_details(channel_name: str, channel_details: dict) -> list:
    old_details: list = []
    channels: list = channel_details.get("Channel_Details")
    if (channels == None):
        print ("\nChannel Details are not available.\n")
    else:
        for channel in channels:
            name: str = channel.get('Name')
            if (name == None):
                print ("\nChannel Names are not available.\n")
            else:
                if (name == channel_name):
                    channel_details: dict =  channel.get('Details')
                    if (channel_details == None):
                        print ("\nChannel Details for " + name +  " are not available.\n")
                    else:
                        sub_count = channel_details.get('Subscriber_Count')
                        video_count = channel_details.get('Video_Count')

                        if (sub_count == None):
                            print ("\nChannel " + name + " subscriber count is not available.\n")
                        else:
                            old_details.insert(0,sub_count)
                        if (video_count == None):
                            print ("\nChannel " + name + " video count is not available.\n")
                        else:
                            old_details.insert(1,video_count)
                    return old_details
                else:
                    continue
    
def compare_channel_details(old_channel_details: dict, new_channel_dict: dict) -> list:
    channel_updates: list = []
    for channel in youtubechannels:
        channel_name: str = channel.name
        new_channels_details: list = get_new_channel_details(channel_name, new_channel_dict)
        old_channels_details: list = get_old_channel_details(channel_name, old_channel_details)
        sub_count_diff: int = int(new_channels_details[0]) - int(old_channels_details[0])
        video_count_diff: int = int(new_channels_details[1]) - int(old_channels_details[1])
        playlist_id: str = new_channels_details[2]
        updates: dict = {"Sub_Count_Diff" : sub_count_diff, "Vid_Count_Diff" : video_count_diff, "Playlist_ID" : playlist_id}
        channel_details: dict = {"Name": channel_name, "Updates" : updates}
        channel_updates.append(channel_details)
        continue
    return channel_updates

def get_latest_videos(diff_list: list) -> list:
    latest_channel_videos: list = []
    for obj in diff_list:
        channel_name: str = obj.get('Name')
        if (channel_name == None):
            print ("\nChannel Names are not available.\n")
        else:
            updates: dict = obj.get('Updates')
            if (updates == None):
                print("\nUpdates Dict is not available.\n")
            else:
                playlist_id: str = updates.get("Playlist_ID")
                if (playlist_id == None):
                    print("\n\Playlist ID is not available.\n")
                else:
                    Vid_count_diff: int = updates.get("Vid_Count_Diff")
                    if (Vid_count_diff == None):
                        print("\nVideo Count Difference is not available.\n")
                    else:
                        if (Vid_count_diff <= 5):
                            new_videos: list = get_playlist_items(playlist_id,5)
                            sorted_videos: list = sort_videos_list_dict(new_videos)
                            videos: dict = {"Channel_Name" : channel_name, "Latest_Videos" : sorted_videos}
                            latest_channel_videos.append(videos)
                        else:
                            new_videos: list = get_playlist_items(playlist_id,Vid_count_diff)
                            sorted_videos: list = sort_videos_list_dict(new_videos)
                            top_five: list = sorted_videos[:5] 
                            videos: dict = {"Channel_Name" : channel_name, "Latest_Videos" : top_five}
                            latest_channel_videos.append(videos)
                        continue
    return latest_channel_videos

def create_main_list(channel_list: list, latest_videos: list, diff_list: list) -> list:
    main: list = []
    for channel in channel_list:
        for video in latest_videos:
            for diff in diff_list:
                channel_name_details_list: str = channel.get("Name")
                channel_name_videos_list: str = video.get("Channel_Name")
                channel_name_diff: str = diff.get("Name")
                
                if (channel_name_details_list == None):
                    print("\nChannel Name is not available in Channel Details List.\n")
                else:
                    if (channel_name_videos_list == None):
                        print("\nChannel Name is not available in Latest Videos List.\n")
                    else:
                        if (channel_name_details_list == channel_name_videos_list):
                            if (channel_name_diff == None):
                                print("\nChannel Name is not available in Difference List.\n")
                            else:
                                if (channel_name_details_list == channel_name_diff):
                                    new_videos: list = video.get("Latest_Videos")
                                    channel_details: dict = channel.get("Details")
                                    updates: list = diff.get("Updates")
                                    
                                    if (new_videos == None):
                                        print("\nLatest Videos is not available in Latest Videos List.\n")
                                    else:
                                        if (channel_details == None):
                                            print("\nChannel Details are not available in Channel Details List.\n")
                                        else:
                                            if (updates == None):
                                                print("\nUpdate Details are not available in Updates List.\n")
                                            else:
                                                temp: dict = {"Name" : channel_name_details_list, "Details" : channel_details, "Latest_Videos" : new_videos, "Updates" : updates}
                                                main.append(temp)
                                                break
                                else:
                                    continue
                        else:
                            continue
            continue
    return main
                
def make_new_file(main_list: list) -> str:
    file_details: dict = {}
    curr_date_time: str = datetime.datetime.utcnow().ctime()
    file_year: str = datetime.datetime.utcnow().strftime("%Y")
    file_month: str = datetime.datetime.utcnow().strftime("%m")
    file_day: str = datetime.datetime.utcnow().strftime("%d")
    file_hour: str = datetime.datetime.utcnow().strftime("%H")
    file_name: str = "channel_details.json"
    file_path: str =  file_year + "/" + file_month + "/" + file_day + "/" + file_hour + "/" + file_name
    file_details["Title"] = "Top 10 Youtube Channels Subcribers Update"
    file_details["Last_Update_Time"] = curr_date_time
    file_details["Channel_Details"] = main_list
    new_json_file: str = json.dumps(file_details, indent=2)
    upload_to_s3(new_json_file, bucket_name, file_path)
    return curr_date_time

def make_latest_file(main_list: list):
     file_details: dict = {}
     curr_date_time: str = datetime.datetime.utcnow().ctime()
     file_name: str = "latest.json"
     file_details["Title"] = "Top 10 Youtube Channels Subcribers Update"
     file_details["Last_Update_Time"] = curr_date_time
     file_details["Channel_Details"] = main_list
     new_json_file: str = json.dumps(file_details, indent=2)
     upload_to_s3(new_json_file,bucket_name,file_name)

def runScript():
    channel_details: list = updateCountJob(youtubechannels)
    channels_sorted_by_subs: list = sort_channels_list_by_Subs(channel_details)
    old_data = read_latest_file()
    diff: list = compare_channel_details(old_data, channels_sorted_by_subs)
    print(" ")
    print(diff)
    print(" ")
    latest_videos: list = get_latest_videos(diff)
    main: list = create_main_list(channels_sorted_by_subs, latest_videos, diff)
    run_time = make_new_file(main)
    make_latest_file(main)
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