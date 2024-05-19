import React, { useState } from 'react';
import LinkInput from './LinkInputs';
import Output from './Output';
import { predict_crawl } from '../../services/prediction-comment';

const Crawl = () => {
  const [userLink, setUserLink] = useState('');
  const [comments, setComments] = useState([]);
  const [algorithm, setAlgorithm] = useState('SVM');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleClearText = () => {
    setUserLink('');
  };

  const handleAlgorithmChange = (event) => {
    setAlgorithm(event.target.value);
  };

  const handleLinkSubmit = async () => {
    setLoading(true);
    setError('');
    try {
      
      console.log(userLink, algorithm);
      const response  = await predict_crawl(userLink, algorithm);
      // console.log(response)
      const [ids, authors, texts, predictions] = response.data;
      console.log(ids, authors, texts, predictions);

      const commentsData = ids.map((id, index) => ({
        id,
        author: authors[index],
        text: texts[index],
        result: predictions[index],
      }));

      setComments(commentsData);
      setUserLink('');
    } catch (error) {
      setError('Error fetching prediction');
      console.error('Error fetching prediction:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center w-full space-y-4">
      <LinkInput value={userLink} onChange={e => setUserLink(e.target.value)} />
      <div className="flex space-x-2">
        <button
          onClick={handleLinkSubmit}
          className="p-2 bg-blue-500 text-white rounded"
          disabled={loading}
        >
          {loading ? 'Submitting...' : 'Submit'}
        </button>
        <button
          onClick={handleClearText}
          className="p-2 bg-gray-500 text-white rounded"
        >
          Clear
        </button>
      </div>

      <select
        id="algorithmSelect"
        value={algorithm}
        onChange={handleAlgorithmChange}
        className="p-2 border border-gray-400 rounded"
      >
        <option value="SVM">SVM</option>
        <option value="ANN">ANN</option>
        <option value="logistic-regression">Logistic Regression</option>
      </select>
      {error && (
        <div className="text-red-500">
          {error}
        </div>
      )}
      <Output comments={comments} />
    </div>
  );
}

export default Crawl;
