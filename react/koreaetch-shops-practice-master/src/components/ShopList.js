import { Fragment, useEffect, useState } from "react";
import axios from "axios";
import Card from "./Card";
import "./ShopList.css";

function ShopList() {
  const [shops, setShops] = useState([]);

  useEffect(() => {
    axios.get("https://api.koreatech.in/shops").then((response) => {
      setShops(response.data.shops);
    });
  }, []);

  return (
    <div className="shop-list_container">
      {shops.map((shop) => (
        <Fragment key={shop.id}>
          <Card
            payCard={shop.pay_card}
            payBank={shop.pay_bank}
            delivery={shop.delivery}
            title={shop.name}
            phone={shop.phone}
            openTime={shop.open_time}
            closeTime={shop.close_time}
          />
        </Fragment>
      ))}
    </div>
  );
}

export default ShopList;
