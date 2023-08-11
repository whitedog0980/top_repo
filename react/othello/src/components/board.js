import styled from "styled-components";
import React, { useState, useRef, useEffect } from "react";
import X_y_to_id from "./x_y_to_id";
import Try_set_chess from "./try_set_chess";
import Can_set_chess from "./can_set_chess";
import { useNavigate } from 'react-router-dom';

const MainDiv = styled.div`
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  width: 100vw;
  height: 96vw;
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
  font-size: 20px;
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

const GameSetSpan = styled.span`
  position: absolute;
  left: 25vw;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50vw;
  height: 30vw;
  background-color: rgba(255,255,255, 0.5);
  backdrop-filter: blur(5px);
  border-radius: 5vw;
  border: 3px solid black;
  box-shadow: 0 0 50px 15px gray;
  font-size: 5vw;
`



const Header = ({set, set_span_proxy, spans}) => {
  const navigate = useNavigate();
  const handleClickSkip = () => {
    set()
  }
  const handleClickRandom = () => {
    const score_board = []
      .concat([90, -5, 50, 10, 10, 50, -5, 90]) // Line 1
      .concat([-5, -9, -2, -2, -2, -2, -9, -5]) // Line 2
      .concat([50, -2, -1, -1, -1, -1, -2, 50]) // Line 3
      .concat([10, -2, -1, -1, -1, -1, -2, 10]) // Line 4
      .concat([10, -2, -1, -1, -1, -1, -2, 10]) // Line 5
      .concat([50, -2, -1, -1, -1, -1, -2, 50]) // Line 6
      .concat([-5, -9, -2, -2, -2, -2, -9, -5]) // Line 7
      .concat([90, -5, 50, 10, 10, 50, -5, 90]);// Line 8

    let can_set = spans.map((chess, id) => {
      if (chess === "neutral_can_put")
        return { id: id, score: score_board[id] };
      return 0;
    });
    can_set = can_set.filter((element) => {
      return element !== 0;
    });
    can_set.sort((a, b) => {
      return b.score - a.score;
    });
    if (!can_set.length) {
      set();
      return;
    };
    can_set = can_set.filter((element) => {
      return element.score === can_set[0].score;
    });

    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }

    set_span_proxy(can_set[getRandomInt(0, can_set.length - 1)].id);
  };
  return (
    <MainHeader>
      <StyledBtn onClick={handleClickSkip} >Skip!</StyledBtn>
      <StyledBtn onClick={handleClickRandom} >AI PUT!</StyledBtn>
      <StyledBtn onClick ={()=>{ navigate('/');}}>Go to Title</StyledBtn>
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
  const [gameSet, setGameSet] = useState(false);

  //Main Logic
  const set_span_proxy = (id) => {
    // skip this click event if there is already a chess at id.
    if ((spans[id] !== "neutral") && (spans[id] !== "neutral_can_put")) return;

    let next_chess = round % 2 === 1 ? "white" : "black"

    let x = id % 8;
    let y = Math.floor(id / 8);
    if (id === 100) {
      x = 100;
      y = 100;
    }

    // skip if we can't set the chess
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

  setSpans(newspans);
  };

  //game set rogic
  const GameSet = ({gameSet}) => {
    if(!gameSet) return <div></div>
    let score = [0,0];
    for (let i = 0; i < 64; i++) {
      if (spans[i] === "black") {score[0] = score[0] + 1}
      if (spans[i] === "white") {score[1] = score[1] + 1}
    }
    if (score[0] > score[1]) {
      return <GameSetSpan>&nbsp;&nbsp;{score[0]} VS {score[1]} <br/> Black Win!</GameSetSpan>
    } else if (score[1] > score[0]) {
      return <GameSetSpan>&nbsp;&nbsp;{score[0]} VS {score[1]} <br/> White Win!</GameSetSpan>
    } else {
      return <GameSetSpan>{score[0]} VS {score[1]} <br/> Draw!</GameSetSpan>
    }
  }


  useEffect(() => {
    let next_chess = round % 2 === 1 ? "white" : "black";
    const newspans = [...spans];

    //delete previous "neutral_can_put"
    for (let i = 0; i < 64; i++) {
      if ((spans[i] === "neutral_can_put")) newspans[i] = "neutral";
    }
    //create new "neutral_can_put"
    Can_set_chess(newspans, next_chess).forEach((changed) => {
      newspans[X_y_to_id(changed.x, changed.y)] = "neutral_can_put";
    })
    //no "neutral" or "neutral_can_put" => gameset
    let game_set = true; 
    for (let i = 0; i < 64; i++) {
      if ((spans[i] === "neutral_can_put") || (spans[i] === "neutral")) {
        game_set = false;
      }
    }
    //no "white" => gameset
    if (game_set === false) {
      game_set = true
      for (let i = 0; i < 64; i++) {
        if ((spans[i] === "white")) {
          game_set = false;
        }
      }
    }
    //no "black" => gameset
    if (game_set === false) {
      game_set = true
      for (let i = 0; i < 64; i++) {
        if ((spans[i] === "black")) {
          game_set = false;
        }
      }
    }
    setGameSet(game_set)

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
      <Header set={() => {setRound(round + 1)}} set_span_proxy={set_span_proxy} spans={spans}></Header>
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
      <GameSet gameSet={gameSet}></GameSet>
    </MainDiv>
  );
}