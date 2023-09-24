import './App.css';
import Table from './component/Table';
import { ChakraProvider, Button } from "@chakra-ui/react"
function App() {
  return (
    <ChakraProvider>
      <div className="App">
        <header className="App-header">
          <h1>testing</h1>
        </header>
        <Table />

      </div>
    </ChakraProvider>

  );
}

export default App;
