import fitz
import pytesseract
import easyocr
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2

# Ensure Tesseract is correctly set up (Windows users must set the path)
# Uncomment and modify the path below if needed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize EasyOCR reader
reader = easyocr.Reader(["en"])


def preprocess_image(image):
    """Enhances image for better OCR accuracy."""
    try:
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresholded = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        return Image.fromarray(thresholded)
    except Exception as e:
        print(f"Error in image preprocessing: {e}")
        return image  # Return the original if error occurs


def extract_text_from_pdf(pdf_path):
    """Extracts text from normal PDFs using PyMuPDF (fitz)."""
    try:
        text = ""
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text("text") + "\n"

        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""


def extract_text_from_images(pdf_path):
    """Extracts text from scanned PDFs using both EasyOCR and Tesseract, selecting the better output."""
    try:
        images = convert_from_path(pdf_path, dpi=300)
        extracted_text = ""

        for i, img in enumerate(images):
            processed_img = preprocess_image(img)

            # Extract text using EasyOCR
            easy_text = reader.readtext(np.array(processed_img), detail=0)
            easy_text = " ".join(easy_text).strip()

            # Extract text using Tesseract
            tesseract_text = pytesseract.image_to_string(processed_img, lang="eng").strip()

            # Choose the method with more extracted text
            best_text = easy_text if len(easy_text) > len(tesseract_text) else tesseract_text
            extracted_text += best_text + "\n"

        return extracted_text.strip()
    except Exception as e:
        print(f"Error extracting text from images: {e}")
        return ""


def extract_text(pdf_path):
    """Extracts text from both normal and scanned PDFs, prioritizing direct extraction."""
    try:
        # First, try extracting text normally
        text_from_pdf = extract_text_from_pdf(pdf_path)

        # If normal text extraction is successful, return it (skip OCR)
        if text_from_pdf.strip():
            return text_from_pdf.strip()

        print("No text found using PyMuPDF, switching to OCR...")
        text_from_images = extract_text_from_images(pdf_path)

        return text_from_images.strip()
    except Exception as e:
        print(f"Error in text extraction process: {e}")
        return ""
