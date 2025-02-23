# AI Webpage Summarizer

This project provides a Python script that utilizes the Hugging Face Transformers library to summarize the content of any webpage using a pre-trained BART model.

## Features

- Summarizes the content of a given webpage URL.
- Uses the `facebook/bart-large-cnn` pre-trained model for summarization.
- Retrieves and processes webpage content using `requests` and `BeautifulSoup` libraries.

## Requirements

To run this script, you need to have Python installed along with the following libraries:

- transformers
- requests
- beautifulsoup4

You can install these libraries using `pip`:

```bash
pip install transformers requests beautifulsoup4
