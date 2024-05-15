import React from 'react';

function TextInput({ userText, setUserText, handlePredict, handleClearText }) {
  const handleTextChange = (event) => {
    setUserText(event.target.value);
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setUserText(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-lg font-bold mb-2">User Text</h2>
      <textarea
        value={userText}
        onChange={handleTextChange}
        rows="20"
        cols="30"
        className="p-2 border border-gray-400 rounded"
      ></textarea>
      <div className="flex space-x-2 mt-2">
        <input
          type="file"
          accept=".txt"
          onChange={handleFileChange}
          className="bg-gray-500 text-white py-1 px-3 rounded"
        />
        <button
          onClick={handleClearText}
          className="bg-red-500 text-white py-1 px-3 rounded"
        >
          Clear
        </button>
        <button
          onClick={handlePredict}
          className="bg-green-500 text-white py-1 px-3 rounded"
        >
          Predict
        </button>
      </div>
    </div>
  );
}

export default TextInput;
