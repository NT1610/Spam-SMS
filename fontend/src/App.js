// src/App.js
import React, { useState } from 'react';
import TextInput from './component/TextInput';
import Predictions from './component/Output';
import { prediction } from './services/prediction-comment';

function App() {
  const [userText, setUserText] = useState('');
  const [comment, setComment] = useState('');
  const [predictionResult, setPredictionResult] = useState('');
  const [algorithm, setAlgorithm] = useState('SVM'); // Định nghĩa biến algorithm và setAlgorithm

  const handleClearText = () => {
    setUserText('');
    setComment('');
    setPredictionResult('');
  };

  const handleAlgorithmChange = (event) => {
    setAlgorithm(event.target.value);
  };

  const handleCommentSubmit = async () => {
    console.log("hello")
    try {
      const response = await prediction(userText, algorithm);
      console.log(response.data)

      const result = response.data === '1' ? 'spam' : 'not spam';
      console.log(result)
      setComment(userText);
      setPredictionResult(result);
    } catch (error) {
      console.error('Error fetching prediction:', error);
      setPredictionResult('Error fetching prediction');
    }
  };

  return (
    <div className="flex flex-col items-center p-5">
      <div className="flex flex-col items-center space-y-2">
        <TextInput
          value={userText}
          onChange={e => setUserText(e.target.value)}
        />
        {/* {console.log(userText)} */}

        <button
          onClick={handleCommentSubmit}
          className="p-2 bg-blue-500 text-white rounded"
        >
          Comment
        </button>


        <button
          onClick={handleClearText}
          className="p-2 bg-gray-500 text-white rounded"
        >
          Clear
        </button>
      </div>
      <div className="flex flex-col items-center space-y-2 mt-4">
        <select
          id="algorithmSelect"
          value={algorithm}
          onChange={handleAlgorithmChange}
          className="p-2 border border-black-400 rounded"
        >
          <option value="SVM">SVM</option>
          <option value="naive-bayes">Naive-Bayes</option>
          <option value="logistic-regression">Logistic Regression</option>
        </select>
      </div>
      {comment && (
        <div className="flex flex-col items-center space-y-2 mt-4">
          <Predictions comment={comment} predictionResult={predictionResult} />
        </div>
      )}
    </div>
  );
}

export default App;
