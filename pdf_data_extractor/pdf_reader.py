import pdfplumber
import pandas as pd
from langdetect import detect
from collections import Counter


class PDFReader:
   """
   A utility class for extracting text and tables from PDF files.
   """

   def __init__(self, file_path):
      """
      Initializes the PDFReader with the path to a PDF file.

      Args:
         file_path (str): The file path to the PDF document.
      """
      self.file_path = file_path

   def extract_text(self, page_num=None):
      """
      Extracts text from the PDF.

      Args:
         page_num (int, optional): The specific page to extract text from.
               If None, extracts text from all pages.

      Returns:
         str or list of str: Text from the specified page or all pages.
      """
      with pdfplumber.open(self.file_path) as pdf:
         if page_num is not None:
               return pdf.pages[page_num].extract_text() or ""
         return [page.extract_text() or "" for page in pdf.pages]

   def extract_tables(self, page_num=None):
      """
      Extracts tables from the PDF.

      Args:
         page_num (int, optional): The specific page to extract tables from.
               If None, extracts tables from all pages.

      Returns:
         list of pd.DataFrame: A list of pandas DataFrames representing tables.
      """
      tables = []
      with pdfplumber.open(self.file_path) as pdf:
         pages = [pdf.pages[page_num]] if page_num is not None else pdf.pages
         for page in pages:
               tables.extend(page.extract_tables())
      return [pd.DataFrame(table) for table in tables if table]
   
   def get_file_statistics(self):
         """
         Calculates and returns statistics about the PDF file.

         Returns:
            dict: A dictionary containing the following statistics:
                  - page_count (int): Total number of pages in the PDF.
                  - total_words (int): Total number of words in the PDF.
                  - total_characters (int): Total number of characters in the PDF.
                  - average_words_per_page (float): Average number of words per page.
                  - average_characters_per_page (float): Average number of characters per page.
         """
         page_count = 0
         total_words = 0
         total_characters = 0

         with pdfplumber.open(self.file_path) as pdf:
            page_count = len(pdf.pages)
            for page in pdf.pages:
                  text = page.extract_text() or ""
                  words = text.split()
                  total_words += len(words)
                  total_characters += len(text)

         return {
            "page_count": page_count,
            "total_words": total_words,
            "total_characters": total_characters,
            "average_words_per_page": total_words / page_count if page_count > 0 else 0,
            "average_characters_per_page": total_characters / page_count if page_count > 0 else 0,
         }
         
   def get_language_statistics(self):
      """
      Analyzes the text in the PDF to determine the distribution of languages.

      Returns:
         dict: A dictionary where keys are language codes (e.g., 'en', 'fr') and 
               values are the percentage of text detected for each language.
      """
      language_counter = Counter()
      total_pages = 0

      with pdfplumber.open(self.file_path) as pdf:
         for page in pdf.pages:
               text = page.extract_text() or ""
               if text.strip():  # Skip empty pages
                  try:
                     language = detect(text)
                     language_counter[language] += 1
                     total_pages += 1
                  except:
                     language_counter["unknown"] += 1  # Handle detection errors

      # Convert counts to percentages
      language_statistics = {
         lang: round((count / total_pages) * 100, 2)
         for lang, count in language_counter.items()
      }

      return language_statistics
