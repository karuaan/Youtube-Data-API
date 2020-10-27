import React  from 'react';
import './App.css';
function Nav() {
    return (
        <nav className="Nav">
            <ul className="Nav-Links">
                <div className="myChannelsNav">
                    <li><a href="/MyChannelsList">My Channels</a></li>
                </div>
                <div className="TopChannelsNav">
                    <li><a href="/TopChannels">Top Channels</a></li>
                </div>
            </ul>
        </nav>
    );
}

export default Nav;