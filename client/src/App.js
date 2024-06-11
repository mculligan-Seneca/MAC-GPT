import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Landing from './components/Landing.js';
import maclog from './assets/MAC_Logo.png';
import { Outlet } from 'react-router-dom';

//TODO: Add react router to application
function App() {
  return (
    <div className="App">
      <div className="container">
        <div className="row d-flex flex-row-reverse">

          <img src={maclog} style={{maxHeight: "100px",maxWidth:"100px"}}/>

        </div>
        <div className="row">
           <Outlet/>
        </div>
          
      </div>
     
    </div>
  );
}

export default App;
