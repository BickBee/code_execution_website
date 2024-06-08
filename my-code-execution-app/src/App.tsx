import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import axios from 'axios';

const App: React.FC = () => {
  const [code, setCode] = useState('print("If you\'re a recruiter, Please Hire Me! :D")');
  const [output, setOutput] = useState('');

  const handleTestCode = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/execute', { code });
      setOutput(response.data.output);
    } catch (error) {
      console.error(error);
      setOutput(`Error executing code: ${error.response ? error.response.data.detail : error.message}`);
    }
  };

  const handleSubmitCode = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/submit', { code });
      setOutput(response.data.message);
    } catch (error) {
      console.error(error);
      setOutput(`Error submitting code: ${error.response ? error.response.data.detail : error.message}`);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="w-full max-w-4xl bg-white shadow-lg rounded-lg p-6">
        <h1 className="text-3xl font-bold mb-6">Code Execution Website - Python 3 - Nicholas Lee</h1>
        <div className="mb-4">
          <Editor
            height="50vh"
            language="python"
            value={code}
            onChange={(value) => setCode(value || '')}
            className="w-full"
          />
        </div>
        <div className="flex space-x-4 mb-4">
          <button onClick={handleTestCode} className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Test Code</button>
          <button onClick={handleSubmitCode} className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Submit</button>
        </div>
        <pre className="bg-gray-200 p-4 rounded-lg">{output}</pre>
      </div>
    </div>
  );
};

export default App;
