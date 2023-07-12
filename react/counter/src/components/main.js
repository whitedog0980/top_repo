import React, { useState, useRef, useEffect } from 'react';
import { BrowserRouter } from 'react-router-dom'
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import styled from 'styled-components'


const MainDiv = styled.div`
height: 300px;
width: 100vw;
display: flex;
justify-content: center;	
align-items: center;
background-color: #d6caff;
`

const MainInput = styled.input`
  height: 70px;
  width: 70px; 
`

const MainBtn = styled.button`
  height: 70px;
  width: 70px; 
`

const SubDiv = styled.div`
height: 300px;
width: 100vw;
display: flex;
justify-content: center;	
align-items: center;
background-color: #d6caff;
`

const SubBtn = styled.button`
  height: 70px;
  width: 70px; 
`

const SubSpan = styled.span`
  display: flex;
  justify-content: center;	
  align-items: center;
  height: 70px;
  width: 70px; 
  background-color: ${props => {
    if (props.counter < 10) {
      return 'green'
    } else if (props.counter >= 10 && props.counter < 20) {
      return 'yellow'
    } else {
      return 'red'
    }
  }}
`



export function Main () {
  const navigate = useNavigate()
  const [number, setNumber] = useState(0)
  const maininputRef = useRef(null)

  const move = () => {
    const inputValue = maininputRef.current.value
    setNumber(inputValue)
    navigate(`/sub/${inputValue}`)
  }


  return (
    <MainDiv>
      <MainInput className="mainInput" ref={maininputRef} />
      <MainBtn className="mainBtn" onClick={move}>이동하기</MainBtn>
    </MainDiv>
  )
}

export function Sub () {
  const { number } = useParams()
  const [counter, setCounter] = useState(0)
  const buttonRef = useRef(null)
  function handleClick() {
    setCounter(Number(counter) + Number(number))
  }

  return (
    <SubDiv>
      <SubBtn ref={buttonRef} onClick={handleClick}>{number}</SubBtn>
      <SubSpan counter={counter} >{counter}</SubSpan>
    </SubDiv>
  )
}



