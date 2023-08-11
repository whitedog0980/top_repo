import './App.css';
import OthelloBoard from './components/board.js';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Opening from './components/opening';


function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Opening />}></Route>
          <Route path='/ongame/' element={<OthelloBoard />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
