import React, { Component } from 'react';
import axios from 'axios';
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

    send_to_node = async(e) =>
    {
        e.preventDefault();

        const { channels } = this.state;
        try
        {
            console.log( channels );
            const response = await fetch( 'http://localhost:1000/channels_list', {
                mode: 'no-cors',
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                Body: { Channels_List: channels }
            } );
            console.log( response )
        }
        catch ( e )
        {
            console.log( e );
        }
    };
   

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
                <button type="button" onClick={this.send_to_node}>Save Channels</button>
            </div>
        );
    }
   
}

export default Form;
