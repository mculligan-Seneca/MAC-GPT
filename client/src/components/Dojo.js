import React, {useState} from 'react';


function Dojo(){

    const [file, setFile]=useState()
    const fileChange=(e)=>{
        setFile(e.target.files[0])
    }
    return (
        <div className="container">
                <div className="row">
                    <p>
                        Please select a document library. 
                    </p>
                </div>
                <div className="row">
                    <div className="col col-md-3">
                        <input id="file_input" type="file" onChange/>
                    </div>
                    <div className='col-md-3 col-offset-4'>
                        <button type="submit"className='btn btn-primary'>Upload</button>
                    </div>
                </div>
        </div>
    );
}

export default Dojo;