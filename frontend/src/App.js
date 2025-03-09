import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [audioUrl, setAudioUrl] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
        responseType: "blob", // Expect an MP3 file
      });

      const url = URL.createObjectURL(response.data);
      setAudioUrl(url);
    } catch (error) {
      alert("Error processing the PDF");
      console.error(error);
    }
  };

  return (
    <div className="app">
      <h1>📄 PDF to Speech Converter 🎙️</h1>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Convert to Audio</button>

      {audioUrl && (
        <div>
          <h2>🔊 Audio Output</h2>
          <audio controls src={audioUrl}></audio>
        </div>
      )}
    </div>
  );
}

export default App;
