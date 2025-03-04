import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from text_extractor import extract_text
from summarizer import summarize_text
import re

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, file_path)

def process_pdf():
    pdf_path = entry_pdf_path.get().strip()
    
    if not pdf_path:
        messagebox.showwarning("Warning", "Please select a PDF file.")
        return
    
    try:
        btn_summarize.config(state=tk.DISABLED)
        summary_text.delete(1.0, tk.END)

        summary_text.insert(tk.END, "Extracting text...\n")
        extracted_text = extract_text(pdf_path)
        extracted_text = re.sub(r"\s+", " ", extracted_text)

        summary_text.insert(tk.END, "Summarizing...\n")
        summary = summarize_text(extracted_text)

        summary_text.delete(1.0, tk.END)
        summary_text.insert(tk.END, summary)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")
    finally:
        btn_summarize.config(state=tk.NORMAL)

root = tk.Tk()
root.title("PDF Summarizer")
root.geometry("700x500")
root.resizable(False, False)

frame_top = tk.Frame(root, padx=10, pady=10)
frame_top.pack(fill=tk.X)

label_pdf = tk.Label(frame_top, text="Select PDF:", font=("Arial", 12))
label_pdf.pack(side=tk.LEFT, padx=(0, 5))

entry_pdf_path = tk.Entry(frame_top, width=50, font=("Arial", 12))
entry_pdf_path.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

btn_browse = tk.Button(frame_top, text="Browse", command=browse_file, font=("Arial", 12))
btn_browse.pack(side=tk.LEFT, padx=5)

btn_summarize = tk.Button(root, text="Summarize PDF", command=process_pdf, font=("Arial", 14), bg="#007BFF", fg="white", padx=10, pady=5)
btn_summarize.pack(pady=10)

summary_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), width=80, height=20)
summary_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()