import React from 'react';
import { Link } from 'react-router-dom';

const Nav = () => {
  return (
    <nav className="w-full p-5 ">
      <ul className="space-y-4">
        <li>
          <Link to="/">
            <button className="w-full p-2 border border-gray-300 rounded bg-white">Spam</button>
          </Link>
        </li>
        <li>
          <Link to="/search">
            <button className="w-full p-2 border border-gray-300 rounded bg-white">Link</button>
          </Link>
        </li>
        <li><button className="w-full p-2 border border-gray-300 rounded bg-white">Xử lí Spam</button></li>
        <li><button className="w-full p-2 border border-gray-300 rounded bg-white">Model Spam</button></li>
      </ul>
    </nav>
  );
}

export default Nav;
