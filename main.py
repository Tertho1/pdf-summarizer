import sys
from text_extractor import extract_text
from summarizer import summarize_text
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    print("\nExtracting text from:", pdf_path)
    extracted_text = extract_text(pdf_path)
    extracted_text = re.sub(r"\s+", " ", extracted_text)

    print("\nSummarizing...\n")
    summary = summarize_text(extracted_text)

    print("\nSummary:\n")
    print("\n".join(summary.split(". ")))

if __name__ == "__main__":
    main()