import './App.css';

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import DataSourceForm from './DataSourceForm';
import ChatPage from './ChatPage';

function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                  <Route path="/chat" element={<ChatPage />} />
                  <Route path="/" element={<DataSourceForm />} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;