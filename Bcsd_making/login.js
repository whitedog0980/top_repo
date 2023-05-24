let id = "whitedog0980@gmail.com";
let password = "minjun6062"
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
let wrongLoginAttempt = 0

// 로그인 화면
const loginBtn = document.getElementById("loginBtn")
loginBtn.addEventListener("click", login);

// 스토리지 저장
loginBtn.addEventListener("click", () => {
  let idInput = document.getElementById("loginInput").value
  let passwordInput = document.getElementById("passwordInput").value
  setCookie(idInput, passwordInput)
  setLocalStorage(idInput, passwordInput)
  setSessionStorage(idInput, passwordInput)
});

function login() {
  let idInput = document.getElementById("loginInput").value
  let passwordInput = document.getElementById("passwordInput").value
  // 로그인 금지 플래그 확인
  const loginFlag = document.cookie.includes('loginBan=true') ////// Changed!!!!!!!!!
  if (loginFlag) {
    alert("잘못된 id/pw를 5회 이상 입력하였습니다. 5번째 잘못입력한 시점에서 1시간 후 로그인이 가능합니다.")
    return
  }

  if (emailRegex.test(idInput)) {
    if ((idInput === id) && (passwordInput === password)) {alert("로그인에 성공했습니다.");}
    else {
      alert("아이디, 비밀번호를 확인해주세요.")
      wrongAttempt()
    }
  }
  else {
    alert("이메일형식을 확인해주세요.")
    wrongAttempt()
  }
}

function wrongAttempt() {
  wrongLoginAttempt = wrongLoginAttempt + 1
  if (wrongLoginAttempt >= 5) { ////// Changed!!!!!!!!!
    setCookie("loginBan", "true") ////// Changed!!!!!!!!!
  }
}

// Cookie 생성 함수
function setCookie(id, password) {
  const expires = new Date();
  expires.setTime(expires.getTime() + 3 * 24 * 60 * 60 * 1000);
  const cookie = `${id}=${password};expires=${expires.toUTCString()};path=/`;
  document.cookie = cookie;
}

// localStorage 생성 함수
function setLocalStorage(id, password) {
  localStorage.setItem(id, password);
}

// sessionStorage 생성 함수
function setSessionStorage(id, password) {
  sessionStorage.setItem(id, password);
}


// 회원가입 화면
//let idRegist = document.getElementById("idRegist").value
//let passwordRegist = document.getElementById("passwordRegist").value
//let passwordRegistCheck = document.getElementById("passwordRegistCheck").value



function student() {
  let studentNumber = document.getElementById()
}