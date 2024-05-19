import React from 'react';
import { Link } from 'react-router-dom';

const Nav = () => {
  return (
    <nav className="w-full p-5 border-r border-gray-300">
      <ul className="space-y-4">
        <li>
          <Link to="/">
            <button className="w-full p-2 border border-gray-300 rounded bg-white">Input Text</button>
          </Link>
        </li>
        <li>
          <Link to="/crawl">
            <button className="w-full p-2 border border-gray-300 rounded bg-white">Input Link</button>
          </Link>
        </li>
        <li>
          <Link to="/">
            <button className="w-full p-2 border border-gray-300 rounded bg-white">About</button>
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Nav;
