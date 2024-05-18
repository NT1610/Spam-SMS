import React from 'react';

const Output = ({ comments }) => {
  return (
    <div className="p-2 border border-gray-300 rounded w-full max-h-96 overflow-y-auto">
      {comments.map((comment, index) => (
        <div key={index} className="mb-2 p-2 border-b border-gray-200">
          <p>{comment.text}</p>
          <p className={comment.result === 'spam' ? 'text-red-500' : 'text-green-500'}>
            {comment.result}
          </p>
        </div>
      ))}
    </div>
  );
};

export default Output;
