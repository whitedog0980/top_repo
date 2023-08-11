import X_y_to_id from "./x_y_to_id";

// "can set chess" algorithm
export default function Try_set_chess(x, y, spans, next_chess) {
  let changed_chesses = [];

  //if you clicked 'Skip!' button
  if (x === 100) {
    return [result, changed_chesses]
  }

  const try_set_chess_side = (x_factor, y_factor) => {
    let want_to_change = [];
    let nx = x + x_factor;
    let ny = y + y_factor;
    let got = false;
    while (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) {
      const chess = spans[X_y_to_id(nx, ny)];
      if ((chess === "neutral") || (chess === "neutral_can_put")) return false;
      if (chess === next_chess) {
        got = true;
        break;
      }
      want_to_change.push({ x: nx, y: ny });
      nx += x_factor;
      ny += y_factor;
    }
    // if con't find any catching type
    if (!got) return false;
    if (Math.abs(nx - x) > 1 || Math.abs(ny - y) > 1) {
      changed_chesses = changed_chesses.concat(want_to_change);
      return true;
    }
    return false;
  };
  let result = false;
  if (try_set_chess_side(-1, 0)) result = true; // left side
  if (try_set_chess_side(1, 0)) result = true; // right side
  if (try_set_chess_side(0, -1)) result = true; // up side
  if (try_set_chess_side(0, 1)) result = true; // down side
  if (try_set_chess_side(-1, -1)) result = true; // left up
  if (try_set_chess_side(-1, 1)) result = true; // left down
  if (try_set_chess_side(1, -1)) result = true; // right up
  if (try_set_chess_side(1, 1)) result = true; // right down

  return [result, changed_chesses];
};