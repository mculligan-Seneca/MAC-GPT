import React, {useState} from 'react';
import axios from 'axios';

const API_URL="http://127.0.0.1:5000/dojo";

function Dojo(){

    const [file, setFile]=useState()
    const handleFileChange=(e)=>{
        setFile(e.target.files[0])
    }
    const onSubmitClick=(e)=>{
        const formData= new FormData();
        formData.append("file",file);
        axios.post(API_URL,formData,{
            headers:{
                "content-type":"multipart/form-data"
            }
        })
        .then(response=>response.json())
        .then(json=>console.log(json));
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
                        <input id="file_input" type="file" onChange={handleFileChange}/>
                    </div>
                    <div className='col-md-3 col-offset-4'>
                        <button type="submit"className='btn btn-primary' onClick={onSubmitClick}>Upload</button>
                    </div>
                </div>
        </div>
    );
}

export default Dojo;