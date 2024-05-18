import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Nav from './component/Nav/Nav';
import Spam from './component/Home/Spam';

function App() {
  return (
    <BrowserRouter>
      <div className="grid grid-cols-5 min-h-screen">
        <div className=" w-full border-r border-gray-300">
          <Nav color="blue-gray" />
        </div>
        <div className="col-span-4 p-5">
          <Routes>
            <Route path="/" element={<Spam />} />
            {/* <Route path="/search" element={<SearchLink />} /> */}
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
