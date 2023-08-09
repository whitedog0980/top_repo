import axios from 'axios';
import { useState, useEffect } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
  useSetRecoilState,
} from 'recoil';

export default function CompleteCheckBox() {
  axios.post('https://api.todoist.com/rest/v2/tasks/2203306141/close',
  null,
  {headers: {
      "Authorization": 'Bearer bc327da6a73022f91148d5ab79387c93ebc1e0bd',
    }}
).then((response) => {
  console.log(response)
})
}

// curl "https://api.todoist.com/rest/v2/tasks/2995104339/close" \
// -X POST \
// -H "X-Request-Id: $(uuidgen)" \
// -H "Authorization: Bearer 0123456789abcdef0123456789"
