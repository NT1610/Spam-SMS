import React, { useState } from 'react';
import TextInput from './component/TextInput';
import Output from './component/Output';
import { prediction } from './services/prediction-comment';

function App() {
  const [userText, setUserText] = useState('');
  const [comments, setComments] = useState([]);
  const [algorithm, setAlgorithm] = useState('SVM');

  const handleClearText = () => {
    setUserText('');
  };

  const handleAlgorithmChange = (event) => {
    setAlgorithm(event.target.value);
  };

  const handleCommentSubmit = async () => {
    try {
      const response = await prediction(userText, algorithm);
      const result = response.data === '1' ? 'spam' : 'not spam';
      const newComment = { text: userText, result };
      setComments([newComment, ...comments]);
      setUserText('');
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

  return (
    <div className="flex flex-col items-center p-5">
      <div className="flex flex-col items-center space-y-2">
        <TextInput
          value={userText}
          onChange={e => setUserText(e.target.value)}
        />
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
          className="p-2 border border-gray-400 rounded"
        >
          <option value="SVM">SVM</option>
          <option value="naive-bayes">Naive-Bayes</option>
          <option value="logistic-regression">Logistic Regression</option>
        </select>
      </div>
      <div className="flex flex-col items-center space-y-2 mt-4 w-full">
        <Output comments={comments} />
      </div>
    </div>
  );
}

export default App;