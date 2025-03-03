from transformers import pipeline

# Load AI summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150, min_length=50):
    """Summarizes extracted text while handling long inputs."""
    if not text.strip():
        return "No text found to summarize."

    chunk_size = 800  # Max input for AI model
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    summary = []
    for chunk in chunks:
        summarized_chunk = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        summary.append(summarized_chunk)
    
    return " ".join(summary)  # Combine all summarized chunks
