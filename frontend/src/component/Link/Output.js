import React from 'react';

const Output = ({ comments }) => {
    return (
        <div className="p-2 border border-gray-300 rounded w-full max-h-96 overflow-y-auto">
            <h1>Comments</h1>
            <table className="w-full">
                <thead>
                    <tr>
                        <th className="border p-2">ID</th>
                        <th className="border p-2">Author</th>
                        <th className="border p-2">Comment</th>
                        <th className="border p-2">Status</th>
                    </tr>
                </thead>
                <tbody>
                    {comments.map((comment, index) => (
                        <tr key={index}>
                            <td className="border p-2">{comment.id}</td>
                            <td className="border p-2">{comment.author}</td>
                            <td className="border p-2">{comment.text}</td>
                            <td className={`border p-2 ${comment.result == '1' ? 'text-red-500' : 'text-green-500'}`}>
                                {comment.result == '1' ? 'Spam' : 'Not Spam'}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Output;
