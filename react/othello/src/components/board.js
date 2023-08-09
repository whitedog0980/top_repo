import styled from "styled-components";
import React, { useState, useRef, useEffect } from "react";
import X_y_to_id from "./x_y_to_id";
import Try_set_chess from "./try_set_chess";
import Can_set_chess from "./can_set_chess";

const MainDiv = styled.div`
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  width: 100vw;
  height: 96vw;
  background-color: gray;
  margin: 0px;
  padding: 0px;
  @media screen and (min-width: 900px) {
    width: 900px;
    height: 850px;
  }
`;

const MainHeader = styled.header`
  display: flex;
  align-items: center;
  justify-content: center;
  justify-content: space-evenly;
  width: 100vw;
  height: 7vh;
  background-color: antiquewhite;
  @media screen and (min-width: 900px) {
    width: 900px;
  }
`

const StyledBtn = styled.button`
  width: calc(10vw + 20px);
  height: calc(3vh + 10px);
  border-radius: 5px;
`

const CellSpans = styled.span`
  align-items: center;
  display: flex;
  width: 12vw;
  height: 12vw;
  background-color: lightgray;
  border: 1px solid black;
  margin: 0px;
  padding: 0px;
  font-size: ${props => (props.props === "neutral_can_put") ? "10vw": 
  (props.props === "black") ? "10vw" : "13vw"};
  @media screen and (min-width: 900px) {
    width: 108px;
    height: 108px;
    font-size:${props => (props.props === "neutral_can_put") ? "90px": 
  (props.props === "black") ? "90px" : "112px"};
  }
`;

const DivChess = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`
const SpanChess = styled.span`
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 0px;
  margin-left: ${props => (props.props === "neutral_can_put") ? "2.5vw": 
  (props.props === "black") ? "-0.78vw" : "0.45vw"};
  margin-bottom: ${props => (props.props === "neutral_can_put") ? "1.9vw": 
  (props.props === "black") ? "1.3vw" : "1.5vw"};
  @media screen and (min-width: 900px) {
    margin-left: ${props => (props.props === "neutral_can_put") ? "22.5px": 
  (props.props === "black") ? "-7.02px" : "4.05px"};
    margin-bottom: ${props => (props.props === "neutral_can_put") ? "17.1px": 
  (props.props === "black") ? "11.7px" : "13.5px"};
  }
`

const Header = ({set}) => {
  const handleClickSkip = () => {
    set()
  }
  const handleClickRandom = () => {
    
  }
  return (
    <MainHeader>
      <StyledBtn onClick={handleClickSkip} ></StyledBtn>
      <StyledBtn onClick={handleClickRandom} ></StyledBtn>
      <StyledBtn></StyledBtn>
      <StyledBtn></StyledBtn>
    </MainHeader>
  )
}


const ChessSpan = ({ order, state, set }) => {
  const getSymbol = (state) => {
    if (state === "black") {
      return "⚫";
    } else if (state === "white") {
      return "○";
    } else if (state === "neutral_can_put") {
      return "+"
    }
    return "　";
  };

  const handleClick = () => {
    set(order);
  };
  return (
    <DivChess
      onClick={handleClick}
    >
      <SpanChess props={state} >{getSymbol(state)}</SpanChess>
    </DivChess>
  );
};

export default function OthelloBoard() {
  const [round, setRound] = useState(0);

  const set_span_proxy = (id) => {
    // skip this click event if there is already a chess at id.
    if ((spans[id] !== "neutral") && (spans[id] !== "neutral_can_put")) return;

    let next_chess = round % 2 === 1 ? "white" : "black"
    let next_2_chess = round % 2 === 0 ? "white" : "black"


    let x = id % 8;
    let y = Math.floor(id / 8);
    if (id === 100) {
      x = 100;
      y = 100;
    }

    // skip if we cant set the chess
    const try_set_chess_return = Try_set_chess(x, y, spans, next_chess)
    if (!try_set_chess_return[0]) return;

    // update the chess board
    let newspans = [...spans];
    try_set_chess_return[1].forEach((changed) => {
      newspans[X_y_to_id(changed.x, changed.y)] = next_chess;
    });
    newspans[id] = next_chess;

    // update round info
    setRound(round + 1);
    if (next_chess === "white") {
      console.log("Next: Black");
    } else {
      console.log("Next: White");
    }

    //delete previous "neutral_can_put"

    // update "neutral_can_put"
  




  setSpans(newspans);
  };

  useEffect(() => {
    let next_chess = round % 2 === 1 ? "white" : "black";
    const newspans = [...spans];

    //delete previous "neutral_can_put"
    for (let i = 0; i < 64; i++) {
      if ((spans[i] === "neutral_can_put")) newspans[i] = "neutral";
    }
    Can_set_chess(newspans, next_chess).forEach((changed) => {
      newspans[X_y_to_id(changed.x, changed.y)] = "neutral_can_put";
    })
    setSpans(newspans);
  }, [round])

  // initialize the OthelloBoard with some chess in the centre.
  let spanstate_first_round = [];
  for (let i = 0; i < 64; i++) {
    if (i === 27 || i === 36) {
      spanstate_first_round.push("black");
    } else if (i === 28 || i === 35) {
      spanstate_first_round.push("white");
    } else {
      spanstate_first_round.push("neutral");
    }
  }

  const [spans, setSpans] = useState(spanstate_first_round);

  return (
    <MainDiv>
      <Header set={() => {setRound(round + 1)}}></Header>
      {spans.map((sp, index) => (
        <CellSpans
        key={"cellspan" + index} 
        props={sp}
        >
          <ChessSpan
            key={"chessspan" + index}
            state={sp}
            order={index}
            set={set_span_proxy}
          />
        </CellSpans>
      ))}
    </MainDiv>
  );
}

