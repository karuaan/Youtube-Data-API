import React, { useState, useRef } from 'react';
import Chevron from './Icons/Chevron.js';

import "./Accordion.css";



function linkCreate(videoID) {
    let urlLink = "https://www.youtube.com/watch?v="+videoID;
    return urlLink
}

function new_checker(value) {
    if (value === "NEW")
    {
        return "Y";
    }

    if (value === "OLD")
    {
        return "N";
    }

    else
    {
        return null;
    }
}

function Accordion(props)
{
    const [setActive, setActiveState] = useState("");
    const [setHeight, setHeightState] = useState("0px");
    const [setRotate, setRotateState] = useState("accordion_icon")
    const content = useRef(null);

    function toggleAccordion() {
        setActiveState(setActive === "" ? "active" : "");
        setHeightState(setActive === "active" ? "0px" : `${content.current.scrollHeight}px`);
        setRotateState(setActive === "active" ? "accordion_icon" : "accordion_icon rotate")
        console.log(content.current.scrollHeight)
    }

    return (
    <div className="accordion_section">
        <button className={`accordion ${setActive}`} onClick={toggleAccordion}>
            <table className="channelDetails">
    <td className="channelName"><b>Channel Name: {props.Name}</b></td>
                <td className="channelSubCount"><b>Subscriber Count: {props.subCount}</b> {props.subDiff}</td>
                <td className="channelVideoCount"><b>Video Count: {props.videoCount}</b> {props.vidDiff}</td>
                <Chevron className={`${setRotate}`} width ={25} height={25} />
            </table>
        </button>
        <div ref={content} style={{maxHeight: `${setHeight}`}} className="accordion_content">
            <div className="video_text">
                <table className="videoDetails">
                    <thead className="videoHeader">
                        <th>Title</th>
                        <th>Is New?</th>
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
                            <td className="videoChecker">{new_checker(video.New_Checker)}</td>
                            <td className="videoViewCount">{video.Video_Details.View_Count}</td>
                            <td className="videoLikeCount">{video.Video_Details.Like_Count}</td>
                            <td className="videoDislikeCount">{video.Video_Details.Dislike_Count}</td>
                            <td className="videoCommentCount">{video.Video_Details.Comment_Count}</td>
                            <td className="videoVideoScore">{video.Video_Details.Video_Score}</td>
                            <td className="videoTime">{video.Video_Details.Published_Time}</td>
                            <td className="videoID"><a href={linkCreate(video.Video_ID)} target="_blank" rel="noopener noreferrer">Video</a></td>
                        </tbody>
                    )}
                </table>
            </div>
        </div>
    </div>
    );
}

export default Accordion;