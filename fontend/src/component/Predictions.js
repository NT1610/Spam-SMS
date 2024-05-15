import React from 'react';

function Predictions({ predictions, handleClearPredictions, handleExport }) {
  return (
    <div className="flex flex-col items-center">
      <h2 className="text-lg font-bold mb-2">Predictions</h2>
      <textarea
        value={predictions}
        readOnly
        rows="20"
        cols="30"
        className="p-2 border border-gray-400 rounded bg-gray-100"
      ></textarea>
      <div className="flex space-x-2 mt-2">
        <button
          onClick={handleExport}
          className="bg-green-500 text-white py-1 px-3 rounded"
        >
          Export
        </button>
        <button
          onClick={handleClearPredictions}
          className="bg-red-500 text-white py-1 px-3 rounded"
        >
          Clear
        </button>
      </div>
    </div>
  );
}

export default Predictions;
