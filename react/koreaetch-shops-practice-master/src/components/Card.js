import "./Card.css";

function Card({ title, phone, openTime, closeTime, payCard, payBank, delivery }) {
  return (
    <div className="card-container" onClick={() => console.log(title)}>
      <div className="card-title">{title}</div>

      <div className="descriptions">
        <div className="description">전화번호 {phone}</div>
        <div className="description">
          운영시간 {openTime} ~ {closeTime}
        </div>
      </div>

      <div className="tags">
        {delivery && <div className="tag">#배달가능</div>}
        {payCard && <div className="tag">#카드가능</div>}
        {payBank && <div className="tag">#계좌이체가능</div>}
      </div>
    </div>
  );
}

export default Card;
