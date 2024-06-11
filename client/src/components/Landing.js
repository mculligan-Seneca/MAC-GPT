
import logo from '../assets/Logo_1_2.png';
import { Link } from 'react-router-dom';
function Landing(){



    return (
        <div className="container">
           
            <div className="row  align-items-center">
                 <img src={logo} style={{maxHeight:"500px",maxWidth:"500px"}}/>
            </div>
            <div className="row text-center d-flex flex-column">
            <h3>Welcome to <span>MacGPT</span>, McMasters own GPT-based advisor</h3>
                 <p>
                    MacGPT is an experimental final-year engineering project
                 </p>
            </div>
            <div className="row">
                <div className="col">
                    <Link to={"/chat"}className="btn btn-dark">CHAT</Link>
                </div>
                <div className="col">
                    <Link to={"/dojo"} className='btn btn-dark'>DOJO</Link>
                </div>
                <div className="col">
                    <Link to={"/online"} className='btn btn-dark'>GO ONLINE</Link>
                </div>

            </div>

        </div>


    );
}


export default Landing;