# СПЕЦІАЛЬНІ МОВИ ПРОГРАМУВАННЯ. Розробка бібліотеки для зчитування датасетів з PDF-файлів. Зеліско Максим та Федоричко Андрій



**PDF Data Extractor** is a Python library designed for working with PDF documents. It provides an easy-to-use interface for extracting text and tables, processing data, and visualizing the structure of pages.

## Features

- Extract text from specific pages or the entire document.
- Extract tables from PDF files and convert them to `pandas.DataFrame`.
- Clean and process text data into structured DataFrames.
- Visualize text and table layouts from specific PDF pages.
- Generate file and language statistics (work in progress).

## Installation

Install the required dependencies with:

```bash
pip install pdfplumber pandas matplotlib

```
## Usage
Initialization
```bash
from pdf_data_extractor import PDFReader, text_to_dataframe, visualize_text_and_tables

# Initialize the PDF reader
pdf_reader = PDFReader("path/to/pdf/file.pdf")
```

Extracting text
```bash
# Extract text from all pages
text_data = pdf_reader.extract_text()

# Extract text from a specific page (e.g., page 0)
text_page_0 = pdf_reader.extract_text(page_num=0)
```
Converting Text to DataFrame
```bash
# Convert text data from all pages into a pandas DataFrame
df = text_to_dataframe(text_data)
```

Visualizing Text and Tables
```bash
# Visualize the structure of text and tables on a specific page (e.g., page 0)
visualize_text_and_tables(pdf_reader, page_num=0)
```

File and Language Statistics(Work in Progress)
```bash
# Get file statistics
stats = pdf_reader.get_file_statistics()

# Get language statistics
language_stats = pdf_reader.get_language_statistics()
```

## Example
```bash
# Initialize the PDFReader
pdf_reader = PDFReader("example.pdf")

# Extract text
text_data = pdf_reader.extract_text()

# Convert text to DataFrame
df = text_to_dataframe(text_data)

# Visualize text and table structure
visualize_text_and_tables(pdf_reader, page_num=0)
```
## LICENSE
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
