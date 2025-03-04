from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150, min_length=50):
    if not text.strip():
        return "No text found to summarize."

    chunk_size = 800
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    summary = []
    for chunk in chunks:
        summarized_chunk = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summary.append(summarized_chunk)
    
    return " ".join(summary)