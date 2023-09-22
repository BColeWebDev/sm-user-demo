import React,{useState,useEffect, Fragment} from 'react';
import axios from "axios"
const Table = () => {
    const [data, setdata] = useState();

    useEffect(() => {
    axios.get('http://localhost:5000/health')
    axios.get('http://localhost:5000/api/users/?page=1&pageSize=100').then((val)=>setdata(val.data))
    }, []);
    return <>User
    <div>
    {data?.data.map((val,idx) => <Fragment key={idx}>
        <p>{val.name}</p>
    </Fragment>)}
    </div>
     </>;
}
 
export default Table;