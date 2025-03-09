from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pyttsx3
import PyPDF2
import os

app = Flask(__name__)
CORS(app)  # Allow frontend requests

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        full_text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

    if not full_text.strip():
        return jsonify({"error": "No readable text found in the PDF"}), 400

    # Convert text to speech
    engine = pyttsx3.init()
    output_file = os.path.join(OUTPUT_FOLDER, "output.mp3")
    engine.save_to_file(full_text, output_file)
    engine.runAndWait()

    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
