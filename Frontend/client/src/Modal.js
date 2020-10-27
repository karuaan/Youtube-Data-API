import React from "react";
import ReactDom from 'react-dom';
import './Modal.css';

const Modal = ({ open, children, onClose }) => {
  
  if ( !open ) return null;

  return ReactDom.createPortal(
    <div className="modal">
      <div className="modal-container">
        { children }
        <button className="modal-close" onClick={onClose}>Save Channels</button>
      </div>
    </div>,
    document.getElementById('portal')
  );
};

export default Modal;