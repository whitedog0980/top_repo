document.addEventListener("DOMContentLoaded", () => {
  const outer = document.getElementById('outer');
  const inner = document.getElementById('inner');

  outer.addEventListener('click', () => {
    console.log('Outer clicked');
  }, true); // 이벤트 캡쳐링 사용

  inner.addEventListener('click', () => {
    console.log('Inner clicked');
  });
});
