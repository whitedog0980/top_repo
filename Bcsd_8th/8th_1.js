let addBtn = document.querySelector("#addSpan")
addBtn.addEventListener("click", createList) // 수정: createList 대신 createList
let isStriked = false


// 리스트 만들기
function createList() {
  console.log("생성")
  const input = document.getElementById("inputList")
  const inputValue = input.value

  // 가장 큰 값의 키 구하기
  const keys = Object.keys(localStorage);
  const maxKey = keys.reduce((max, currentKey) => {
    const numericCurrentKey = parseInt(currentKey, 10);
    return numericCurrentKey > max ? numericCurrentKey : max;
  }, 0); // 초기 값을 0으로 설정
  // maxKey가 -Infinity인 경우를 처리
  const nextKey = isFinite(maxKey) ? maxKey + 1 : 0;

  let listItem = {
    value: inputValue,
    isStriked: false
  };

  localStorage.setItem(nextKey, JSON.stringify(listItem));
  sync()
}

// 동기화
function sync() {
  const mainDiv = document.querySelector("#mainDiv")
  mainDiv.innerHTML = ""; // 수정: 기존의 리스트를 초기화

  // 가장 큰 키값 구하기
  const keys = Object.keys(localStorage);
  // 가장 큰 값의 키 구하기
  const maxKey = keys.reduce((max, currentKey) => {
    const numericCurrentKey = parseInt(currentKey, 10);
    return numericCurrentKey > max ? numericCurrentKey : max;
  }, 0); // 초기 값을 0으로 설정

  // maxKey가 -Infinity인 경우를 처리
  const nextKey = isFinite(maxKey) ? maxKey + 1 : 0;

  for (let i = 0; i < maxKey + 1; i++) {
    const inputList = localStorage.getItem(i)
    if (inputList === null) {continue}
    let inputIndex = JSON.parse(inputList)

    const listOdject = document.createElement("div")
    const index = document.createElement("span")
    const btns = document.createElement("span")
    const completeBtn = document.createElement("span")
    const deleteBtn = document.createElement("span")
    listOdject.className = "lists"
    index.className = "index"
    btns.className = "btns"
    completeBtn.className = "completeBtn"
    deleteBtn.className = "deleteBtn"
    if (inputIndex.isStriked === true) {
      index.classList.add("strikeout")
    }

    // 취소줄 추가/삭제 이벤트 리스너
    completeBtn.addEventListener("click", () => {
      if (inputIndex.isStriked === true) {
        inputIndex.isStriked = false
        localStorage.setItem(i, JSON.stringify(inputIndex));
        index.classList.remove("strikeout")
      } else {
        inputIndex.isStriked = true
        localStorage.setItem(i, JSON.stringify(inputIndex));
        index.classList.add("strikeout")
      }
    })
    // 삭제 이벤트 리스너
    deleteBtn.addEventListener("click", () => {
      localStorage.removeItem(i)
      sync()
    });
    index.textContent = inputIndex.value
    mainDiv.appendChild(listOdject)
    listOdject.appendChild(index)
    listOdject.appendChild(btns)
    btns.appendChild(completeBtn)
    btns.appendChild(deleteBtn)
  }
}

// function deleteList(i) {
//   localStorage.removeItem(i)

//   sync()
// }

sync()
