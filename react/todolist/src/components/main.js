import { useState } from 'react';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
  useSetRecoilState,
} from 'recoil';



const todoListState = atom({
  key: 'todoListState',
  default: [],
});

export default function TodoList() {
  const todoList = useRecoilValue(todoListState)
  
  return (
    <>
      {}
      {}
      <TodoItemCreater />

      {todoList.map((todoItem) => (
        <TodoItem key={todoItem.id} item={todoItem} />
      ))}
    </>
  )
}

function TodoItemCreater() {
  const [inputValue, setInputvalue] = useState('');
  const setTodoList = useSetRecoilState(todoListState)
  const [id, setId] = useState(0)

  const addItem = () => {
    setTodoList((oldTodoList) => [
      ...oldTodoList,
      {
        id: id,
        text: inputValue,
        isComplete: false,
      },
    ])
    setId((prevId) => prevId + 1)
    setInputvalue('')
  }

  const onChange = ({target: {value}}) => {
    setInputvalue(value)
  }

  return (
    <div>
      <input type='text' value={inputValue} onChange={onChange}></input>
      <button onClick={addItem}>Add</button>
    </div>
  )

}

function TodoItem({item}) {
  const [todoList, setTodoList] = useRecoilState(todoListState)
  const index = todoList.findIndex((listItem) => listItem === item)

  const editItemText = ({target: {value}}) => {
    const newList = replaceItemAtIndex(todoList, index, {
      ...item,
      text: value,
    })

    setTodoList(newList)
  }

  const toggleItemCompletion = () => {
    const newList = removeItemAtIndex(todoList, index, {
      ...item,
      isComplete: !item.isComplete
    })

    setTodoList(newList)
  }

  const deleteItem = () => {
    const newList = removeItemAtIndex(todoList, index)

    setTodoList(newList)
  }


  return (
    <div>
      <input type='text' value={item.text} onChange={editItemText}></input>
      <input
        type='checkbox'
        checked={item.isComplete}
        onChange={toggleItemCompletion}
      />
      <button onClick={deleteItem}>삭제</button>
    </div>
  )
}

function replaceItemAtIndex(arr, index, newValue) {
  return [...arr.slice(0, index), newValue, ...arr.slice(index + 1)]
}

function removeItemAtIndex(arr, index) {
  return [...arr.slice(0, index), ...arr.slice(index + 1)]
}