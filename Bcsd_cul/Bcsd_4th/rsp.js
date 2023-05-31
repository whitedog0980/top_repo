

let isReseted = true;
let randRsp = null;
let playerSelect = null;
let randomNum = Math.floor(Math.random() * 3) + 1;
const $rock = document.getElementById("R")
const $scissor = document.getElementById("S")
const $paper = document.getElementById("P")

$rock.style.display = "none";
$scissor.style.display = "none";
$paper.style.display = "none";

function selectRock() {
  playerSelect = 1
}
function selectScissor() {
  playerSelect = 2
}
function selectPaper() {
  playerSelect = 3
}

function randReset() {
  randomNum = Math.floor(Math.random() * 3) + 1;
}

function Reset() {
  $rock.style.display = "none"
  $scissor.style.display = "none";
  $paper.style.display = "none";
}

function gameSet() {
  if (randomNum === 1) {
    $rock.style.display = "block";
    $scissor.style.display = "none";
    $paper.style.display = "none";
  }
  if (randomNum === 2) {
    $rock.style.display = "none";
    $scissor.style.display = "block";
    $paper.style.display = "none";
  }
  if (randomNum === 3) {
    $rock.style.display = "none";
    $scissor.style.display = "none";
    $paper.style.display = "block";
  }
}

function gameResult() {
  if (playerSelect === randomNum) {alert("비겼습니다!")}
  if (((playerSelect === 1) && (randomNum === 2)) || ((playerSelect === 2) && (randomNum === 3)) || ((playerSelect === 3) && (randomNum === 1))) {alert("이겼습니다!")}
  if (((playerSelect === 1) && (randomNum === 3)) || ((playerSelect === 2) && (randomNum === 1)) || ((playerSelect === 3) && (randomNum === 2))) {alert("졌습니다!")}
}