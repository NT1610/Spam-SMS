import React from 'react';

const TextInput = ({ value, onChange }) => {
  return (
    <>
      <textarea
        value={value}
        onChange={onChange}
        rows="4"
        cols="50"
        className="p-2 border border-gray-300 rounded"
        placeholder="Enter your comment here..."
      />
    </>
  );
};

export default TextInput;
