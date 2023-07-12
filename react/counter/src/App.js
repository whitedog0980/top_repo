import { Routes, Route, BrowserRouter } from "react-router-dom";
import './App.css';
import { Main, Sub } from "./components/main";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/sub/:number" element={<Sub />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
