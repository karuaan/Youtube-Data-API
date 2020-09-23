import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
import CountIncrease from './Icons/CountIncrease.js';
import CountDecrease from './Icons/CountDecrease.js';
import CountEqual from './Icons/CountEqual.js';

function differenceHelper(differenceNumber)
{
  if (differenceNumber > 0)
  {
    return <div> <CountIncrease width={12} height={15} /> {differenceNumber} </div>;
  } else if (differenceNumber < 0) {

    let non_negative = differenceHelper*-1;
    
    return <div> <CountDecrease width={12} height={15}  /> {non_negative} </div>;


  } else {
    return <div><CountEqual width={12} height={15} fill={"#842DCE"}/> {differenceNumber} </div> ;
  }
}

class App extends Component{

  constructor(props) {
    // Call our fetch function below once the component mounts
  super(props);

  this.state = {
    error: null,
    latest_update_time: null,
    channel_details: []
  };
}

componentDidMount()
{
  fetch('/express_backend')
  .then(res => res.json())
  .then(
    (result) => {
      this.setState(
        {
          latest_update_time: result.Last_Update_Time,
          channel_details: result.Channel_Details
        }
      );
    },
    (error) => {
      this.setState({
        error
      });
    }
  )
}

  render(){
    const { error, latest_update_time, channel_details } = this.state;
    if (error)
    {
    return <div>Error: {error}.message</div>
    }

    return (
      <div className="App">
        {/* <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header> */}
      
        <h1 className="mainTitle">Top 11 Channels by Subscribers</h1>
        <ol type="2" className="ChannelsList">
          {channel_details.map(
              channel =>
                <li key = {channel.Name} className="ChannelDetails">
                    <p className="ChannelName">Channel Name: {channel.Name}</p> 
                    <p className="subCount">Subscribers: {channel.Details.Subscriber_Count} {differenceHelper(channel.Updates.Sub_Count_Diff)} </p> 
                    <p className="videoCount"> Video Count: {channel.Details.Video_Count}     {differenceHelper(channel.Updates.Vid_Count_Diff)} </p>               
                </li>
            )}
        </ol>
        <h5>Last Update: {latest_update_time}</h5>
        </div>
    );
  }
} 

export default App;
