import React, { Component } from 'react';
//import logo from './logo.svg';
import CountIncrease from './Icons/CountIncrease.js';
import CountDecrease from './Icons/CountDecrease.js';
import CountEqual from './Icons/CountEqual.js';
import Accordion from './Accordion.js';
import Modal from './Modal.js';
import Form from './Form.js';
// import FormSheet from './FormSheet.js';

function differenceHelper(differenceNumber)
{
  if (differenceNumber > 0)
  {
    return <span className="increaseNumber"><CountIncrease width={25} height={20} /> {differenceNumber} </span>;
  } else if (differenceNumber < 0) {
    
    return <span className="decreaseNumber"> <CountDecrease width={25} height={20}  /> {Math.abs(differenceNumber)} </span>;


  } else {
    return <span className="sameNumber"><CountEqual width={20} height={15} /> {differenceNumber}</span>;
  }
}
  
  
class MyChannelsListHelper extends Component {
  constructor(props) {
    // Call our fetch function below once the component mounts
    super( props );


  this.state = {
    error: null,
    latest_update_time: null,
    isOpen: false,
    channel_details: []
  };
  }
  
  
OnClickPopup()  {
  this.setState(
    {
      isOpen: true
    })
} 

onClickClose() {
  this.setState(
    {
      isOpen: false
    })
}

componentDidMount()
{
  fetch('/userchannels')
  .then(res => res.json())
  .then(
    (result) => {
    console.log(result);
        this.setState(
            {
            latest_update_time: result.Last_Update_Time,
              isOpen: false,
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
  let data = fetch('/userchannels').then(res => res.json());

  return data;
}

  render() {
    const { error, latest_update_time, isOpen, channel_details } = this.state;
    if (error)
    {
    return <div>Error: {error}.message</div>
    }


    if (latest_update_time === "No Channels Added!") 
    {
      return (
            <div className="App">
                <body>
                    <h1 className="mainTitle">My Channels</h1>
                    <h2>{ channel_details.Name }</h2>

            <button onClick={() => this.OnClickPopup()}>Add New Channel</button>
            <Modal open={ isOpen } onClose={() => this.onClickClose()}>
              <Form />
            </Modal>
                </body>
                <footer>
                    <h3 className="lastUpdate">Last Update: {latest_update_time}</h3>
                </footer>
            </div>
        );
    }
    else {
        return (
            <div className="App">
           
              <body>
              <h1 className="mainTitle">My Channels</h1>
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
              <button onClick={() => this.OnClickPopup()}>Add New Channel</button>
            <Modal open={ isOpen } onClose={() => this.onClickClose()}>
                <Form />
            </Modal>
              </body>
              <footer>
                <h3 className="lastUpdate">Last Update: {latest_update_time}</h3>
              </footer>
              </div>
          );
    }
  }
} 
export default MyChannelsListHelper;
