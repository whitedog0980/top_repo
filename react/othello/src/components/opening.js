import styled from "styled-components";
import React, { useState, useRef, useEffect } from "react";
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';


const OpeningDiv = styled.div`
  display: flex; 
  flex-direction: column;
  align-items: center;
  justify-content: center; 
  width: 100vw;
  height: 60vw;
  background-color: beige;
`
const BtnsDiv = styled.div`
  display: flex; 
  width: 50vw;
  align-items: center;
  justify-content: center; 
  justify-content: space-evenly;
`
const StyledBtn = styled.button`
  width: calc(12vw + 20px);
  height: calc(3vh + 10px);
  border-radius: 5px;
  font-size: 2vw;
`
const HowToPlayDiv = styled.div`
  display: flexbox;
  width: 70vw;
  height: 70vw;
  background-color: white;
  border-radius: 2vw;
  border: solid black 1px;
`
const StyledImg = styled.img`
  width: 40vw;
  height: 11vw;
`
const StyledP = styled.p`
  font-size: 1.8vw;
`

export default function Opening() {
  const navigate = useNavigate();
  const [isClicked, setIsClicked] = useState(false);
  const Start = () => {
    return <StyledBtn onClick ={()=>{ navigate('/ongame/');}}>Game Start!</StyledBtn>
  }
  const HowToPlay = () => {
    if (isClicked) return <HowToPlayDiv>
      <StyledP>오셀로 게임은 많은 돌을 자신의 색깔로 바꾸면 이기는 게임입니다.</StyledP>
      <StyledP>자신의 돌과 같은 줄에(대각선 포함) 연속해서 상대의 돌이 존재한다면,<br/> 반대편 끝에 자신의 돌을 넣을 수 있습니다.</StyledP>
      <StyledImg src=".\othello_example1.png" />
      <StyledP>(+가 있는곳에 둘 수 있습니다.)</StyledP>
      <StyledImg src=".\othello_example2.png"/>
      <StyledP>+ 를 클릭하게 된다면 이렇게 사이에 있는 돌을 자신의 돌로 바꿀 수 있습니다.</StyledP>
      <StyledP><br/> 게임 특성상, 구석에 있는 돌이 뒤집어지기 어려우므로, 우선해서 확보할 필요가 있습니다.</StyledP>
      <StyledP><br/> 특정 알고리즘으로 컴퓨터가 놓게 할 수 있는 "AI PUT!" 버튼이 있으므로,<br /> 혼자서 플레이 하는것도 가능합니다!</StyledP>
    </HowToPlayDiv>
    else return <div></div>
  }
  return <OpeningDiv>
    <h1>오셀로 게임</h1>
    <BtnsDiv>
      <Start></Start>
      <StyledBtn onClick={() => {
        if (isClicked) {setIsClicked(false)}
        else {setIsClicked(true)}
      }}>How to play?</StyledBtn>
    </BtnsDiv>
    <HowToPlay></HowToPlay>
  </OpeningDiv>
}