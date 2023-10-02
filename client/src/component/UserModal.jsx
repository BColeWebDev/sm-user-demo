import React, { useEffect, useState } from 'react';
import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    Button,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    useDisclosure,
    Text
  } from '@chakra-ui/react'
import { getUser } from '../services/userSevices';
const UserModal = ({isOpen, onToggle,ID}) => {
    
    const [ModalData, setModalData] = useState();
   useEffect(() => {
    if(ID !== ""){
    getUser(ID).then((val)=> setModalData(val.data))
    }
   }, [ID]);
    return <>
    <Modal isOpen={isOpen} onClose={onToggle}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>User Id {ModalData?.id}</ModalHeader>
          <ModalCloseButton />
          <ModalBody display={"flex"} flexDir={"column"}>
            <Text>{ModalData?.firstName}</Text>
            <Text> {ModalData?.lastName}</Text>
            <Text>{ModalData?.email}</Text>
            <Text> {ModalData?.timeZone}</Text>
          </ModalBody>

          <ModalFooter>
            <Button colorScheme='blue' mr={3} onClick={onToggle}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>;
}
 
export default UserModal;