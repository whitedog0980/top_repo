import styled from 'styled-components'
import React, { useState } from 'react';

const Nav = styled.nav`
background-color: aliceblue;
display: flex;
align-items: center;
justify-content: center;
`

const MainDiv = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 500px;
  background-color: aqua;
`

const Labels = styled.label`
width: 70vw;
background-color: aliceblue;
display: flex;
align-items: center;
justify-content: center;
`

const Input = styled.input`
width: 70vw;
background-color: aliceblue;
display: flex;
align-items: center;
justify-content: center;
margin-bottom: 30px;
`

const Button = styled.button`
width: 70vw;
background-color: aliceblue;
display: flex;
align-items: center;
justify-content: center;
`

const Table = styled.table`
width: 400px;
margin-top: 40px;
border: 1px solid black;
`
const TableHead = styled.th`
border: 1px solid black;
`
const TableRow = styled.tr`
border: 1px solid black;
`
const TableData = styled.td`
border: 1px solid black;
`

export default function Register() {
  const [formState, setFormState] = useState({
    id : "",
    pw : "",
    pw2 : "",
    name : ""
  })

  const [tableData, setTableData] = useState([])

  const handleChange = (e) => {
    const value = e.target.value
    setFormState({
      ...formState,
      [e.target.name] : value
    })
  }

  const submit = () => {
    setTableData([...tableData, formState])

  }

  return (
    <>
      <Nav>상단바</Nav>
      <MainDiv>
        <Labels>아이디</Labels>
        <Input onChange={handleChange} value={formState.id} name="id"></Input>
        <Labels>비밀번호</Labels>
        <Input onChange={handleChange} value={formState.pw} name="pw"></Input>
        <Labels>비밀번호 확인</Labels>
        <Input onChange={handleChange} value={formState.pw2} name="pw2"></Input>
        <Labels>이름</Labels>
        <Input onChange={handleChange} value={formState.name} name="name"></Input>
        <Button onClick={submit}>제출</Button>
        <Table>
          <thead>
            <TableRow>
              <TableHead>아이디</TableHead>
              <TableHead>비밀번호</TableHead>
              <TableHead>이름</TableHead>
            </TableRow>
          </thead>
          <tbody>
            {tableData.map(data => (
              <TableRow key={data.id}>
                <TableData>{data.id}</TableData>
                <TableData>{data.pw}</TableData>
                <TableData>{data.name}</TableData>
              </TableRow>
            ))}
          </tbody>
        </Table>
      </MainDiv>
    </>
    
  )
}