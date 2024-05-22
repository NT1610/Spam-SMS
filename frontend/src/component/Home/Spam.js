import React, { useState } from 'react';
import TextInput from './TextInput';
import Output from './Output';
import { prediction } from '../../services/prediction-comment';

const Spam = () => {
    const [userText, setUserText] = useState('');
    const [comments, setComments] = useState([]);
    const [algorithm, setAlgorithm] = useState('SVM');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleClearText = () => {
        setUserText('');
    };

    const handleAlgorithmChange = (event) => {
        setAlgorithm(event.target.value);
    };

    const handleCommentSubmit = async () => {
        setLoading(true);
        setError('');
        try {
            console.log(userText)
            const response = await prediction(userText, algorithm);
            const result = response.data == '1' ? 'spam' : 'not spam';
            const newComment = { text: userText, result };
            setComments([newComment, ...comments]);
            setUserText('');
        } catch (error) {
            setError('Error fetching prediction');
            console.error('Error fetching prediction:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex flex-col items-center w-full space-y-4">
            <TextInput value={userText} onChange={e => setUserText(e.target.value)} />

            {console.log(algorithm)}
            <div className="flex space-x-2">
                <button
                    onClick={handleCommentSubmit}
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
                className= "fixed top-32 right-10 p-2 border border-gray-400 rounded"
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

export default Spam;
