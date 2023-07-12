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
    <>
      {(isLoginVisible && isRegisterVisible) && (
        <div id="mainMenu">
          <a href="#" onClick={handleLoginClick} className="btn btn-info topLink">login</a>
          <a href="#" onClick={handleRegisterClick} className="btn btn-light topLink">register</a>
        </div>
      )}
      {!isLoginVisible && <Login />}
      {!isRegisterVisible && <Register />}
    </>
  )
}

export default Top;

