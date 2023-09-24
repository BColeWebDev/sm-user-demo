import React,{useState,useEffect, Fragment} from 'react';
import axios from "axios"
import {
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    Spinner,
    TableCaption,
    Box,
    TableContainer,
    Button,Text, Select, 
  } from '@chakra-ui/react'
const Tables = () => {
    const [data, setdata] = useState();
    const [page, setpage] = useState(1);
    const [pageItems, setpageItems] = useState(100);
    const [isLoading, setIsLoading] = useState(false);
    const [input, setinput] = useState("");
    useEffect(() => {
        setIsLoading(true)
    axios.get('http://127.0.0.1:5000/health')

    axios.get(`http://127.0.0.1:5000/api/users/?page=${page}&pageSize=${pageItems}`).then((val)=>{
 setIsLoading(false)
    setdata(val.data)
})
    }, [page,pageItems]);
    console.log(data)
    return <>
    <Box>
        
    <TableContainer>
  <Table variant="striped">
  <TableCaption position={"fixed"} bottom="0" bg={"gray.300"} w={"100%"}><Box display={"flex"} alignItems={"center"} w={"100%"} justifyContent={"center"}>

  <Button  mx={4}  isDisabled={page <= 1? true : false} onClick={()=>setpage(1)}>{"<<"}</Button>
   <Button isDisabled={page <= 1? true : false} onClick={()=>setpage( page <= 1 ? 1 : page -1)}>{"<"}</Button>


 <Box  display={"flex"}alignItems={"center"}>
    <Text mx={2}>{data?.pageNumber} out of {data?.totalPages}</Text>
   
    <Select  bg={"white"} mx={4} w={"200px"} onChange={(e)=>{
        setIsLoading(true)
        setpageItems(e.target.value)
    }}>
    {[10,25,100,1000].map((val)=><option key={val}value={val} >Display{val}</option>)}
    </Select>
 </ Box>

<Button isDisabled={page === data?.totalPages ? true :false}  mx={4} onClick={()=>setpage( page  + 1)}>{">"}</Button>
<Button  isDisabled={page === data?.totalPages ? true :false}  mx={4} onClick={()=>setpage(data?.totalPages)}>{">>"}</Button>


</Box>
</TableCaption>
    <Thead position={"fixed"} top="0" bg={"yellow"} w={"100%"} display={"flex"} justifyContent={"space-between"}>
    <Tr display={"flex"} width={"100%"}>
        
        {data?.tableHeaders?.map((val,idx)=>
        
            <Th flex={0.75} textAlign={"center"} key={idx}>{val.name}</Th>
       )}
    </Tr>
      
    </Thead>
    {isLoading ? <Box minH={"100vh"} display={"flex"} justifyContent={"center"} alignItems={"center"}><Spinner/> </Box>:    <Tbody maxH={"100px"} overflow={"auto"}>
     {data?.data?.map((tableBody,idx)=><>
        <Tr key={idx}>{data.tableHeaders.map((val,key)=> <Td key={key}>{tableBody[`${val.value}`]}</Td>)}</Tr>
     </>)}  
    </Tbody>}
 
  </Table>
</TableContainer>



    </Box>
     </>;
}
 
export default Tables;