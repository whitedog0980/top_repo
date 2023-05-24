function setCookie(name, value, days) {
  // 만료 시간 설정
  const expires = new Date();
  expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000); // 현재 시각으로 부터 24시간 후
  // 쿠키 생성
  const cookie = `${name}=${encodeURIComponent(value)};expires=${expires.toUTCString()};path=/`;
  document.cookie = cookie;
}

