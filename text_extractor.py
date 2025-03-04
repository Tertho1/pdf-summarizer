import fitz
import pytesseract
import easyocr
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

reader = easyocr.Reader(["en"])

def preprocess_image(image):
    try:
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresholded = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        return Image.fromarray(thresholded)
    except Exception as e:
        print(f"Error in image preprocessing: {e}")
        return image

def extract_text_from_pdf(pdf_path):
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
    try:
        images = convert_from_path(pdf_path, dpi=300)
        extracted_text = ""

        for i, img in enumerate(images):
            processed_img = preprocess_image(img)

            easy_text = reader.readtext(np.array(processed_img), detail=0)
            easy_text = " ".join(easy_text).strip()

            tesseract_text = pytesseract.image_to_string(processed_img, lang="eng").strip()

            best_text = easy_text if len(easy_text) > len(tesseract_text) else tesseract_text
            extracted_text += best_text + "\n"

        return extracted_text.strip()
    except Exception as e:
        print(f"Error extracting text from images: {e}")
        return ""

def extract_text(pdf_path):
    try:
        text_from_pdf = extract_text_from_pdf(pdf_path)

        if text_from_pdf.strip():
            return text_from_pdf.strip()

        print("No text found using PyMuPDF, switching to OCR...")
        text_from_images = extract_text_from_images(pdf_path)

        return text_from_images.strip()
    except Exception as e:
        print(f"Error in text extraction process: {e}")
        return ""