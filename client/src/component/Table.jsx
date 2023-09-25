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
    useDisclosure,
    Box,
    TableContainer,
    Link,
  
    Button,Text, Select, RadioGroup, Radio, 
  } from '@chakra-ui/react'
import { GetAllUser } from '../services/userSevices';
import{BsChevronDoubleLeft, BsChevronDoubleRight, BsChevronLeft,BsChevronRight} from "react-icons/bs"
import UserModal from './UserModal';
import{Link as ReactLink}from "react-router-dom"
const Tables = ({search,setsearch}) => {
    const [data, setdata] = useState();
    const [page, setpage] = useState(1);
    const [pageItems, setpageItems] = useState(10);
    const [isLoading, setIsLoading] = useState(false);
    const [sort, setsort] = useState("");
    const { isOpen,onToggle } = useDisclosure()
    const [ID, setID] = useState("");


  // 
  const displayModal = (tableBody,tableHeader)=>{
    return   <Td fontWeight={"medium"} cursor={"pointer"} onClick={()=>{
      setID(tableBody[`${tableHeader.value}`])
      onToggle()
    }}> 
    {tableBody[`${tableHeader.value}`]}
    </Td>
  }

    useEffect(() => {
        // set spinner for loading
        setTimeout(()=>{
     setIsLoading(true)
      GetAllUser(page,pageItems,search,sort).then((val)=>{
      setIsLoading(false)
      setdata(val.data)
        },20000)
 
})
    }, [page,pageItems,search,sort]);
   
    return <>
    <Box>

    {/* Pagination Top */}
    {data !== undefined?
    <Box  bg={"#1A365D"} position={"sticky"} w={"100%"} alignItems={"center"}  top={"48px"} display={"flex"} justifyContent={"center"}>
     
     
     <Box ml={3} display={"flex"} justifyContent={"center"}>
     <Button  mx={4}  isDisabled={page <= 1? true : false} onClick={()=>setpage(1)}><BsChevronDoubleLeft/></Button>
  <Button isDisabled={page <= 1? true : false} onClick={()=>setpage( page <= 1 ? 1 : page -1)}>{<BsChevronLeft/>}</Button>


<Box  display={"flex"}alignItems={"center"} >
   <Text color={"white"} mx={2}>{data?.pageNumber} out of {data?.totalPages}</Text>
  
   <Select  bg={"white"} mx={4} w={"200px"} onChange={(e)=>{
       setIsLoading(true)
       setpageItems(e.target.value)
   }}>
   {[10,25,100,1000].map((val)=><option key={val}value={val} >Display{val}</option>)}
   </Select>
</ Box>

<Button isDisabled={page === data?.totalPages ? true :false}  mx={4} onClick={()=>setpage( page  + 1)}><BsChevronRight/></Button>
<Button  isDisabled={page === data?.totalPages ? true :false}  mx={4} onClick={()=>setpage(data?.totalPages)}>{<BsChevronDoubleRight/>}</Button>
     </Box>
     
   <Text fontWeight={"bold"} color={"white"}>{`Total Count: ${data?.totalCount}`}</Text>
   <RadioGroup value={sort} onChange={setsort}><Radio mx={2} value='firstName:asc' colorScheme={"blue"}>A-Z</Radio><Radio  colorScheme={"blue"} value='firstName:desc'>Z-A</Radio></RadioGroup>
   </Box> : null}
   

        
    <TableContainer>
  <Table variant="striped">
    <Thead  bg={"gray.300"}>
    <Tr >
        
        {data?.tableHeaders?.map((val,idx)=>
        
            <Th flex={0.75} textAlign={"center"} key={idx}>{val.name}</Th>
       )}
    </Tr>
      
    </Thead>
    {isLoading ? <Box minH={"100vh"} w={"100%"} display={"flex"} justifyContent={"center"} alignItems={"center"}><Spinner/> </Box>:    <Tbody maxH={"100px"} overflow={"auto"}>
     {data?.data?.map((tableBody,idx)=><Fragment key={idx}>
        <Tr key={idx}>{data.tableHeaders.map((tableHeader,key)=> 
        <Fragment key={key}>
          {tableHeader.name === "ID" ?
          displayModal(tableBody,tableHeader)
          :
          <Td fontWeight={"medium"} key={key} >{tableBody[`${tableHeader.value}`]}</Td>

          }
        </Fragment>
        )}
        </Tr>
     </Fragment>)}  
    </Tbody>}
 
  </Table>
    </TableContainer>


    </Box>
    <UserModal isOpen={isOpen} onToggle={onToggle} ID={ID}/>
     </>;
}
 
export default Tables;