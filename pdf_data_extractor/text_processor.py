import pandas as pd


def clean_text(text):
   """
   Cleans and removes extra spaces from the text.

   Args:
      text (str): The input text to clean.

   Returns:
      str: Cleaned text.
   """
   if text:
      return " ".join(text.split())
   return ""

def text_to_dataframe(text_list):
   """
   Converts a list of page texts into a pandas DataFrame.

   Args:
      text_list (list of str): A list containing text from each page.

   Returns:
      pd.DataFrame: DataFrame created from the text data.
   """
   data = []
   for page_text in text_list:
      if page_text:  # Ensure the text is not empty
         lines = page_text.split("\n")  # Split text into lines
         for line in lines:
               cleaned_line = clean_text(line)
               data.append(cleaned_line.split(","))  # Split by commas
   return pd.DataFrame(data, columns=data[0])  # Use the first line as column headers
