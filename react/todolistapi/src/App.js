import './App.css';
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
  useSetRecoilState,
} from 'recoil';
import Main from './components/main';


function App() {
  return (
    <RecoilRoot>
      <Main />
    </RecoilRoot>
  );
}

export default App;
