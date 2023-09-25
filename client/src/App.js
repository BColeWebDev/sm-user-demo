import { useState } from 'react';
import './App.css';
import Navbar from './component/Navbar';
import Table from './component/Table';
import { ChakraProvider } from "@chakra-ui/react";
import {
  BrowserRouter 
} from "react-router-dom";

function App() {
  
  const [search, setsearch] = useState("");
  return (
    <BrowserRouter>
      <ChakraProvider>
      <div className="App">
        <header className="App-header">
         <Navbar search={search} setsearch={setsearch}/>
        </header>
        <Table search={search} setsearch={setsearch} />

      </div>
    </ChakraProvider>
    </BrowserRouter>
  

  );
}

export default App;
