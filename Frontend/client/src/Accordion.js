import React from 'react';
import Chevron from './Icons/Chevron.js';

import "./Accordion.css";

function linkCreate(videoID) {
    let urlLink = "https://www.youtube.com/watch?v="+videoID;
    return urlLink
}

function Accordion(props)
{
    return (
    <div className="accordion_section">
        <button className="accordion">
            <table className="channelDetails">
                <td className="channelName">Channel Name: {props.Name}</td>
                <td className="channelSubCount">Subscriber Count: {props.subCount} {props.subDiff}</td>
                <td className="channelVideoCount">Video Count: {props.videoCount} {props.vidDiff}</td>
                <td className="chevron"><Chevron width = {12} height={20} /></td>
            </table>
        </button>
        <div className="accordion_content">
            <div className="video_text">
                <table className="videoDetails">
                    <thead className="videoHeader">
                        <th>Title</th>
                        <th>View Count</th>
                        <th>Like Count</th>
                        <th>Dislike Count</th>
                        <th>Comments Count</th>
                        <th>Video Score</th>
                        <th>Publish Time</th>
                        <th>Link</th>
                    </thead>
                    {props.videoDetails.map (
                        video =>
                        <tbody className="videoInformation">
                            <td className="videoTitle">{video.Video_Details.Title}</td>
                            <td className="videoViewCount">{video.Video_Details.View_Count}</td>
                            <td className="videoLikeCount">{video.Video_Details.Like_Count}</td>
                            <td className="videoDislikeCount">{video.Video_Details.Dislike_Count}</td>
                            <td className="videoCommentCount">{video.Video_Details.Comment_Count}</td>
                            <td className="videoVideoScore">{video.Video_Details.Video_Score}</td>
                            <td className="videoTime">{video.Video_Details.Published_Time}</td>
                            <td className="videoID"><a href={linkCreate(video.Video_ID)}>Video</a></td>
                        </tbody>
                    )}
                </table>
            </div>
        </div>
    </div>
    );
}

export default Accordion;