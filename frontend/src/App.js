import './App.css';
import { useEffect } from 'react';
import { BrowserRouter } from 'react-router-dom'
import axios from 'axios';
import AllRoutes from './routes/AllRoutes.jsx';

function App() {
  
  useEffect(() => {
    axios.get('http://localhost:8000/api/initialize')
      .catch(error => {
        console.log('Something went wrong!');
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <BrowserRouter>
          <AllRoutes />
        </BrowserRouter>
        
      </header>
    </div>
  );
}

export default App;
