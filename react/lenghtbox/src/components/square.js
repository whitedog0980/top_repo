import React, { useState, useRef, useEffect } from 'react';
import './square.css'

function Square() {
  const Box = useRef(null);
  const [boxWidth, setBoxWidth] = useState(null);
  const [clicked, setClicked] = useState(0);

  useEffect(() => {
    setBoxWidth(Box.current.offsetWidth);
  }, [clicked]);

  const handleButtonClick = () => {
    setClicked(clicked + 1)
  };

  return (
    <div id="sq" ref={Box}>
      <span id="span">{"<-----"}{boxWidth}{"----->"}</span>
      <button id="button" onClick={handleButtonClick}>
        측정하기!
      </button>
    </div>
  );
}

export default Square;