import React, { useState } from 'react';
import './beforeMig/css.css';
import Login from './login';
import Register from './register';

function Top() {
  const [isLoginVisible, setIsLoginVisible] = useState(true);
  const [isRegisterVisible, setIsRegisterVisible] = useState(true);

  const handleLoginClick = () => {
    setIsLoginVisible(false);
    setIsRegisterVisible(true);
  }

  const handleRegisterClick = () => {
    setIsRegisterVisible(false);
    setIsLoginVisible(true);
  }

  return (
    <div id="mainMenu">
      {isLoginVisible && (<a href="#" onClick={handleLoginClick} className="btn btn-info topLink">login</a>)}
      {isRegisterVisible && (<a href="#" onClick={handleRegisterClick} className="btn btn-light topLink">register</a>)}
      {!isLoginVisible && <Login />}
      {!isRegisterVisible && <Register />}
    </div>
  )
}

export default Top;

