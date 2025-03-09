# PDF-Audio

📌 Project Description

The PDF to Speech Converter is a Python-based application that allows users to convert text from a PDF document into spoken audio using a text-to-speech (TTS) engine. The application leverages Tkinter's file dialog to select a PDF file, PyPDF2 to extract text from the document, and pyttsx3 to convert the extracted text into speech.

This tool is particularly useful for users who want to listen to PDFs instead of reading them, making it accessible for individuals with visual impairments or those who prefer auditory learning.

🚀 Features

📂 Select a PDF File: Users can choose a PDF from their system using a file dialog.

🔍 Extract Text: The program extracts text from each page of the PDF.

🗣 Convert Text to Speech: The extracted text is read aloud using the pyttsx3 library.

⚡ Efficient Processing: The text-to-speech engine is initialized only once to improve performance.

🔊 Supports Continuous Reading: Reads the entire document in sequence without interruptions.

🛠 Tech Stack

Python 🐍

PyPDF2 📄 (for extracting text from PDF)

pyttsx3 🗣 (for text-to-speech conversion)

Tkinter 🎛 (for file selection dialog)
