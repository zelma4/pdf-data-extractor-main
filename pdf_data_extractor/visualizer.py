import pdfplumber
import matplotlib.pyplot as plt

def visualize_text_and_tables(reader, page_num):
   """
   Visualizes the structure of text and tables on a specified page.

   Args:
      reader (PDFReader): An instance of the PDFReader class.
      page_num (int): The page number to visualize.
   """
   with pdfplumber.open(reader.file_path) as pdf:
      page = pdf.pages[page_num]
      image = page.to_image()
      image.debug_tablefinder()
      plt.imshow(image.annotated)
      plt.axis('off')
      plt.show()
