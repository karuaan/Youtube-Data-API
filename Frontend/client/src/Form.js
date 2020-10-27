import React, { Component } from 'react';

import './Form.css';

class Form extends Component
{
    constructor(props)
    {
        super(props);

        this.state = {
            error: null,
            channels: [],
            channel_obj: {
                channel_id: ''
            }
        };

        this.handleInput = this.handleInput.bind(this);
        this.addItems = this.addItems.bind(this);
    }


    handleInput(cid) {
        this.setState({
            channel_obj:{
                channel_id: cid.target.value
            }
        })
    }

    handleCheck(val) {
        if ( this.state.channels.includes( val ) )
        {
            return true;
        }
        return false;
    }

    addItems(cid) {
        cid.preventDefault();

        const newItem = this.state.channel_obj.channel_id;
        console.log( newItem );
        
        if ( newItem !== "" )
        {

            const newItemChecker = this.handleCheck( newItem );
            if ( newItemChecker === false )
            {
            const new_channels = [ ...this.state.channels, newItem ];

            this.setState( {
                channels: new_channels,
                channel_obj: { channel_id: ''}
            })
            }
            
            else
            {
                this.setState( {
                    channel_obj: { channel_id: ''}
                } )
            }
        }
    }

    render()
    {
        const { error, channels } = this.state;

        if (error)
        {
            return <div>Error: {error}.message</div>
        }

        return (
            <div className="channelsForm">
                <form id="channels_form" onSubmit={ this.addItems }> 
                    <h2>Add Channels to List!</h2>
                    <lable for="cid">Channel ID: </lable>
                    <input type="text" id="cid" name="cid" value={this.state.channel_obj.channel_id} onChange={this.handleInput}/><br/><br/>
                    <button type="submit">Add Channel</button>
                </form>
                <div className="formDisplay">
                    <h3>Current Channels</h3>
                    <div className="channelsList">
                    { channels.map(
                        channel => 
                            <p>{ channel }</p>
                         )}
                    </div>
                </div>

            </div>
        );
    }
   
}

export default Form;