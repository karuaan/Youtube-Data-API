import React from 'react';
//import logo from './logo.svg';
import './App.css';
// import CountIncrease from './Icons/CountIncrease.js';
// import CountDecrease from './Icons/CountDecrease.js';
// import CountEqual from './Icons/CountEqual.js';
// import Accordion from './Accordion.js';
import Nav from './Nav.js';
import TopChannels from './TopChannels.js';
import MyChannelsListHelper from './MyChannelsListHelper.js';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
//import Form from './Form.js';

function App() {
    return (
      <Router>
        <div className="App">
          <Nav/>
          <Switch>
            <Route path="/" exact component={MyChannelsListHelper} />
            <Route path="/TopChannels" component={TopChannels} />
            <Route path="/MyChannelsList" component={MyChannelsListHelper} />
          </Switch>
        </div>
      </Router>
    );
  }

export default App;
