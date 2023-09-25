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
    useDisclosure
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
          <ModalHeader>User Id {ModalData.id}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
          {ModalData.firstName}
          {ModalData.lastName}
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