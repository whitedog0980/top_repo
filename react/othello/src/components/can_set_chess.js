import X_y_to_id from "./x_y_to_id";

// check can we put
export default function Can_set_chess(newspans, next_2_chess) {
  let can_set_list = []
  const can_set_chess_side = (x_factor, y_factor, ix, iy) => {
    let nx = ix + x_factor;
    let ny = iy + y_factor;
    let got = false;
    while (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) {
      const chess = newspans[X_y_to_id(nx, ny)];
      if ((chess === "neutral") || (chess === "neutral_can_put")) return false;
      if (chess === next_2_chess) {
        got = true;
        break;
      }
      nx += x_factor;
      ny += y_factor;
    }
    if (!got) return false;
    if (Math.abs(nx - ix) > 1 || Math.abs(ny - iy) > 1) {
      return true;
    }
    return false
  }

  for (let i = 0; i < 64; i++) {
    const ix = i % 8;
    const iy = Math.floor(i / 8);
    if ((newspans[i] !== "neutral") && (newspans[i] !== "neutral_can_put")) {
      continue
    }
    let result = false;
    if (can_set_chess_side(-1, 0, ix, iy)) result = true; // left side
    if (can_set_chess_side(1, 0, ix, iy)) result = true; // right side
    if (can_set_chess_side(0, -1, ix, iy)) result = true; // up side
    if (can_set_chess_side(0, 1, ix, iy)) result = true; // down side
    if (can_set_chess_side(-1, -1, ix, iy)) result = true; // left up
    if (can_set_chess_side(-1, 1, ix, iy)) result = true; // left down
    if (can_set_chess_side(1, -1, ix, iy)) result = true; // right up
    if (can_set_chess_side(1, 1, ix, iy)) result = true; // right down
    if (result) {
      can_set_list.push({ x: ix, y: iy })
    }
  }
  return can_set_list
}