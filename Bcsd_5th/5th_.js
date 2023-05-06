const data = [
  { id: "id:1", name: "사과", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes1.jpg"},
  { id: "id:2", name: "수박", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes2.jpg"},
  { id: "id:3", name: "바나나", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes3.jpg"},
  { id: "id:4", name: "배", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes4.jpg"},
  { id: "id:5", name: "체리", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes5.jpg"},
  { id: "id:6", name: "아보카도", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes6.jpg"},
  { id: "id:7", name: "딸기", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes7.jpg"},
  { id: "id:8", name: "오랜지", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes8.jpg"},
  { id: "id:9", name: "복숭아", imgPath: "C:/Users/User/Desktop/top_repo/top_repo/images/frutes9.jpg"}
]

const div_all_buttons = document.querySelector("#mainDiv");
const subDiv_all_buttons = document.querySelector("#subDiv")

for(let i = 0; i < 9; i++) {
  const items = document.createElement("span");
  const img = document.createElement("img");
  img.src = data[i].imgPath ;
  img.className = "imgs"
  items.innerHTML = data[i].name;
  items.className = "items";
  items.classList.add("Button" + data[i].id);
  // appendChild
  div_all_buttons.appendChild(items);
  items.appendChild(img);
  // 클릭했을때
  items.addEventListener("click", () => {
    if (items.parentNode === document.querySelector("#mainDiv")) {
      items.remove();
      img.remove();
      items.className = "items2"
      items.classList.add("Button" + data[i].id)
      img.className = "imgs2"
      subDiv_all_buttons.appendChild(items)
      items.appendChild(img);
    }else if (items.parentNode === document.querySelector("#subDiv")) {
      items.remove();
      img.remove();
      items.className = "items"
      items.classList.add("Button" + data[i].id)
      img.className = "imgs"
      div_all_buttons.appendChild(items)
      items.appendChild(img);
    }
  })
}

const buttons = document.querySelectorAll("span")

