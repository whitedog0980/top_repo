let interval
let time
let isOn = false
let isprogress = false
let freezeTime = 0

document.getElementById("startButton").addEventListener("click", startClicked)
document.getElementById("freButton").addEventListener("click", waiting)
const digitDiv = document.getElementById("digit") 

// 클릭했을 떄
function startClicked() {
    time = 300
    if (isOn === false) {
      progress()
      isOn = true
    }
}

// 진행중
function progress() {
  digitDiv.style.color = "white";
  if (isprogress === false) {
    isprogress = true
    interval = setInterval(timeNotice, 1000)
  }

  function timeNotice() {
    if (time > 0) {
      console.log(`${time} left`);
      digitDiv.textContent = `${culTime(time)}`;
      time = time - 1;
    } else {
      clearInterval(interval);
      digitDiv.textContent = `Time Over!`
      isOn = false
    }
  }
}


// freze 버튼 클릭됨
async function frezeClicked() {
  const fivesec = new Promise((resolve, reject) => {
    let id = setTimeout(() => {
      if (id === interval) {
        resolve(true)
      }
      else {
        reject(false)
      }
    } ,5000)
    interval = id
  })
  digitDiv.style.color = "blue"
}

async function waiting() {
  clearTimeout(interval)
  frezeClicked().then(progress)
}   


// 분 초 계산
function culTime(time) {
  let sec = time
  let min = 0
  while (sec > 59) {
    sec = sec - 60
    min = min + 1
  }
  if (sec > 9) {return `${min} : ${sec}`}
  else {return `${min} : 0${sec}`}
}