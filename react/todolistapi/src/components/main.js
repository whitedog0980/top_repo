import { useState, useEffect } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
  useSetRecoilState,
} from 'recoil';
import axios from 'axios';
import styled from 'styled-components';

const TodoDiv = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: auto;
  height: 30px;
  background-color: wheat;
`;

const todoListAtom = atom({
  key: 'todoList',
  default: [],
});

export default function Main() {
  const [todoList, setTodoList] = useRecoilState(todoListAtom);

  useEffect(() => {
    axios
      .get('https://api.todoist.com/rest/v2/tasks?project_id=2315921219', {
        headers: {
          Authorization: 'Bearer bc327da6a73022f91148d5ab79387c93ebc1e0bd',
        },
      })
      .then(({ data }) => setTodoList(data));
  }, []);

  console.log(todoList)

  return (
    <div>
      {todoList.map((todo) => (
        <TodoDiv key={todo.id}>
          {todo.content}
        </TodoDiv>
      ))}
    </div>
  );
}
