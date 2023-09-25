import React from 'react';
import{Box, Text,Input,InputGroup,InputRightElement } from "@chakra-ui/react"
import { BiUser, BiSearch} from 'react-icons/bi';
const Navbar = ({search,setsearch}) => {




    return <Box bg={"#1A365D"} display={"flex"}  alignItems={"center"} justifyContent={"space-between"} padding={3}><Text color={"white"} fontWeight={"bold"}>Smartsheet Demo </Text>
   {/* <InputGroup maxW={"500px"}>
    <InputRightElement pointerEvents='none'>
      <BiSearch color='gray'/>
    </InputRightElement>
    <Input bg="white" value={search}
    //  onChange={(e)=>setsearch(e.target.value)}
      type='text' 
      placeholder='Search' />
  </InputGroup>
    <BiUser color='white' fontSize={"20px"}/> */}
    </Box>;
}
 
export default Navbar;