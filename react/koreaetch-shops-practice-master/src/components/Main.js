import "./Main.css";
import ShopCategory from "./ShopCategory";
import ShopList from "./ShopList";

function Main() {
  return (
    <div className="container">
      <h1 className="title">주변 상점</h1>
      <ShopCategory />
      <ShopList />
    </div>
  );
}

export default Main;
