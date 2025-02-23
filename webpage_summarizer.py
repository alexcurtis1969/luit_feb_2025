"""Script for using AI Summarizer for any webpage"""
import os
import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer

# Disable symlink warning
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

def summarize_text(text, max_length=150, min_length=30, num_beams=4):
    """
    Summarize the input text using the provided model and tokenizer.
    
    Args:
        text (str): The input text to be summarized.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
        num_beams (int): Number of beams for beam search.
    
    Returns:
        summary (str): The generated summary of the input text.
    """
    # Tokenize the input text
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)

    # Generate the summary
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        num_beams=num_beams,
        length_penalty=2.0,
        early_stopping=True
    )

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def get_webpage_text(url):
    """
    Retrieve and extract text content from a web page.
    
    Args:
        url (str): The URL of the web page.
    
    Returns:
        text (str): The extracted text content from the web page.
    """
    # Get the web page content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text from the web page
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text

if __name__ == "__main__":
    # Prompt user to enter a URL
    url = input("Enter the URL of the web page to summarize: ")

    # Retrieve the web page content
    web_page_text = get_webpage_text(url)

    # Summarize the web page content
    summary = summarize_text(web_page_text)
    
    # Print the summary
    print("Summary:", summary)