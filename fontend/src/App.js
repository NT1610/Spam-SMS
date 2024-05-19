import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Nav from './component/Nav/Nav';
import Spam from './component/Home/Spam';
import Crawl from './component/Link/Crawl'; // Import the new Crawl component
import { SiFacebook } from "react-icons/si";

function App() {
  return (
    <>
      <div className="fixed top-4 right-4 flex flex-col items-center">
        <SiFacebook size={50} color="blue" />
        <span className="text-xl font-bold text-blue-600 mt-2">Facebook spam comment</span>
      </div>
      <BrowserRouter>
        <div className="grid grid-cols-5 min-h-screen">
          <div className="col-span-1 w-full border-r border-gray-300 bg-blue-950">
            <Nav />
          </div>
          <div className="col-span-4 p-5 bg-gray-100">
            <Routes>
              <Route path="/" element={<Spam />} />
              <Route path="/crawl" element={<Crawl />} /> 
            </Routes>
          </div>
        </div>
      </BrowserRouter>
    </>
  );
}

export default App;
