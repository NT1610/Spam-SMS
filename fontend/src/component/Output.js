import React from 'react';

const Predictions = ({ comment, predictionResult }) => {
  return (
    <div className="p-2 border border-gray-300 rounded">
      <h3>Comment:</h3>
      <p>{comment} <span className={`text-${predictionResult === 'spam' ? 'red' : 'green'}-500`}>{predictionResult}</span></p>
    </div>
  );
};

export default Predictions;
