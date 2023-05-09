let id = "whitedog0980@gmail.com";
let password = "minjun6062"
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
// 로그인 화면
const loginBtn = document.getElementById("loginBtn")
loginBtn.addEventListener("click", login);

function login() {
  let idInput = document.getElementById("loginInput").value
  let passwordInput = document.getElementById("passwordInput").value
  if (emailRegex.test(idInput)) {
    if ((idInput === id) && (passwordInput === password)) {alert("로그인에 성공했습니다.");}
    else {alert("아이디, 비밀번호를 확인해주세요.")}
  }
  else {alert("이메일형식을 확인해주세요.")}
}

// 회원가입 화면
let idRegist = document.getElementById("idRegist").value
let passwordRegist = document.getElementById("passwordRegist").value
let passwordRegistCheck = document.getElementById("passwordRegistCheck").value



function student() {
  let studentNumber = document.getElementById()
}
