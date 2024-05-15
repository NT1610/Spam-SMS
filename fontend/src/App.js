import React, { useState } from 'react';
import './App.css';
import TextInput from './component/TextInput';
import Predictions from './component/Predictions';

function App() {
  const [userText, setUserText] = useState('');
  const [predictions, setPredictions] = useState('');
  const [algorithm, setAlgorithm] = useState('svm');

  const handleClearText = () => {
    setUserText('');
  };

  const handleClearPredictions = () => {
    setPredictions('');
  };

  const handleAlgorithmChange = (event) => {
    setAlgorithm(event.target.value);
  };

  const handlePredict = () => {
    if (userText.trim() === '') {
      alert('Please enter some text to predict');
      return;
    }

    const lines = userText.split('\n');
    const newPredictions = lines.map((line) => {
      const isSpam = Math.random() > 0.5;
      return `${isSpam ? '[1]' : '[0]'} ${line}`;
    });

    setPredictions(newPredictions.join('\n'));
  };

  const handleExport = () => {
    const blob = new Blob([predictions], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'predictions.txt';
    link.click();
  };

  return (
    <div className="flex flex-col items-center p-5">
      <div className="flex flex-col items-center space-y-2">
        <label htmlFor="algorithmSelect" className="font-bold">
          Choose an algorithm
        </label>
        <select
          id="algorithmSelect"
          value={algorithm}
          onChange={handleAlgorithmChange}
          className="p-2 border border-black-400 rounded"
        >
          <option value="svm">SVM</option>
          <option value="other">Other</option>
        </select>
      </div>
      <div className="flex space-x-10 mb-5">
        <TextInput
          userText={userText}
          setUserText={setUserText}
          handlePredict={handlePredict}
          handleClearText={handleClearText}
        />
        <Predictions
          predictions={predictions}
          handleClearPredictions={handleClearPredictions}
          handleExport={handleExport}
        />
      </div>

    </div>
  );
}

export default App;
