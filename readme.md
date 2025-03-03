# PDF Summarizer

This project extracts text from PDFs (both regular and scanned) and summarizes the extracted content using AI-powered text summarization.

## Features

- Extracts text from normal PDFs using `PyMuPDF` (fitz).
- Extracts text from scanned PDFs using `Tesseract OCR` and `EasyOCR`.
- Preprocesses images for better OCR accuracy.
- Summarizes extracted text using the `facebook/bart-large-cnn` model from `transformers`.
- Handles large text inputs by processing in chunks.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.8+
- `pymupdf`
- `pytesseract`
- `pdf2image`
- `easyocr`
- `Pillow`
- `torch`
- `transformers`

### Additional Requirements

- **Tesseract OCR**:  
  Install Tesseract OCR and ensure it is correctly set up.  
  Windows users may need to set the path in `text_extractor.py`:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```
- **Poppler** (For `pdf2image` to work):
  - Windows: Install from [this link](https://github.com/oschwartz10612/poppler-windows/releases) and add it to the system `PATH`.
  - Linux: Install using:
    ```bash
    sudo apt install poppler-utils
    ```
  - macOS: Install using:
    ```bash
    brew install poppler
    ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tertho1/pdf-summarizer.git
   cd pdf-summarizer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with a PDF file as an argument:

```bash
python main.py path/to/document.pdf
```

To Run the gui version

```bash
python gui_main.py
```

Or simply run it from you IDE and choose a pdf to summarize it

### Example Output

```text
Extracting text from: sample.pdf

Extracted Text (Preview - First 1000 chars):

Lorem ipsum dolor sit amet, consectetur adipiscing elit...

Summarizing...

Summary:

- The document discusses key aspects of Lorem Ipsum.
- Various elements and structure are explained concisely.
```

## File Structure

```
pdf-summarizer/
│── main.py              # Main script to run extraction and summarization
│── text_extractor.py    # Handles text extraction from PDFs (regular & scanned)
│── summarizer.py        # AI-based text summarization
│── requirements.txt     # Required Python packages
│── README.md            # Project documentation
```
