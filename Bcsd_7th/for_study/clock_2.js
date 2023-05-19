let interval;
let time = 300;
let isOn = false;
let isPaused = false;

document.getElementById("startButton").addEventListener("click", startClicked);
document.getElementById("freButton").addEventListener("click", pauseClicked);
const digitDiv = document.getElementById("digit");

function startClicked() {
  if (!isOn) {
    isOn = true;
    progress();
  }
}

function progress() {
  if (isPaused) return;
  
  digitDiv.style.color = "white";
  digitDiv.textContent = `${culTime(time)}`;
  
  interval = setInterval(() => {
    if (time > 0) {
      time--;
      digitDiv.textContent = `${culTime(time)}`;
    } else {
      clearInterval(interval);
      digitDiv.textContent = "Time Over!";
      isOn = false;
    }
  }, 1000);
}

function pauseClicked() {
  if (isOn) {
    if (!isPaused) {
      clearInterval(interval);
      digitDiv.style.color = "blue";
      isPaused = true;
      setTimeout(() => {
        isPaused = false;
        progress();
      }, 5000);
    }
  }
}

function culTime(time) {
  const minutes = Math.floor(time / 60);
  const seconds = time % 60;
  const formattedMinutes = minutes.toString().padStart(2, "0");
  const formattedSeconds = seconds.toString().padStart(2, "0");
  return `${formattedMinutes}:${formattedSeconds}`;
}
