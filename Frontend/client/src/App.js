import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
import CountIncrease from './Icons/CountIncrease.js';
import CountDecrease from './Icons/CountDecrease.js';
import CountEqual from './Icons/CountEqual.js';
import Accordion from './Accordion.js';

function differenceHelper(differenceNumber)
{
  if (differenceNumber > 0)
  {
    return <span className="increaseNumber"><CountIncrease width={12} height={14} /> {differenceNumber} </span>;
  } else if (differenceNumber < 0) {

    let non_negative = differenceHelper*-1;
    
    return <span className="decreaseNumber"> <CountDecrease width={12} height={13}  /> {non_negative} </span>;


  } else {
    return <span className="sameNumber"><CountEqual width={12} height={12} /> {differenceNumber}</span>;
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
  );
}

fetchData() {
  let data = fetch('/express_backend').then(res => res.json());

  return data;
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
               <li> 
                    <Accordion Name={channel.Name}  
                               subCount={channel.Details.Subscriber_Count} 
                               videoCount={channel.Details.Video_Count} 
                               subDiff={differenceHelper(channel.Updates.Sub_Count_Diff)} 
                               vidDiff={differenceHelper(channel.Updates.Vid_Count_Diff)} 
                               videoDetails={channel.Latest_Videos}
                               /> 
                </li>
            )}
        </ol>
        <h3 className="lastUpdate">Last Update: {latest_update_time}</h3>
        </div>
    );
  }
} 

export default App;
