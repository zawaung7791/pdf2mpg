import PyPDF2
from gtts import gTTS
import os

# function 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

# function 2: Convert text to speech and save as MP3
def text_to_speech(text, output_path):
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save(output_path)

# Main function
def convert(pdf_path, output_path):
    print("Extracting text")
    text = extract_text_from_pdf(pdf_path)
    print("Converting speech to MP3")
    text_to_speech(text, output_path)
    print(f"Conversion complete. MP3 saved at '{output_path}'")

if __name__ == "__main__":
    pdf_path = "./files/onedrive.pdf"  # Provide the path to the input PDF file
    output_path = "./outputs/onedrive.mp3"  # Provide the desired path for the output MP3 file
    
    convert(pdf_path, output_path)
