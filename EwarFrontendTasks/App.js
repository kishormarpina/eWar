import './App.css';
import React from 'react';
import {useState} from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';


function App() {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  let bodyHtml = <div>
    <p>This is sample Dynamic body</p>
  </div>
  return (
    <div className="App">
      <div>
      <center>
      <h2>Click to Open Modal</h2>
        <button className="main_button" name="button" onClick={handleShow}>click here</button>
      </center>
      </div>
  
      <Modal bodyHtml={bodyHtml} show={show} onHide={handleClose} backdrop="static">
        <Modal.Header closeButton>
          <Modal.Title>Modal title</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {bodyHtml}
        </Modal.Body>
        <Modal.Footer>
        <Button variant="success"  onClick={handleClose}>
            Agree
          </Button>
          <Button variant="danger" onClick={handleClose}>
            Cancel
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default App;
