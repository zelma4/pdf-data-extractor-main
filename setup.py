from setuptools import setup, find_packages

setup(
   name="pdf_data_extractor", 
   version="0.1.0",
   description="A Python package for extracting text and tables from PDF files.",
   author="Fedorychko Andrii, Zelisko Maksym, and New Author",
   author_email="fedorychko78@gmail.com, maksonchannel135@gmail.com",
   url="https://github.com/andriifed77/pdf-data-extractor",
   packages=find_packages(),
   install_requires=[
      "pdfplumber>=0.11.4",
      "pandas>=2.1.0",
      "matplotlib>=3.7.2"
   ],
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
   python_requires=">=3.8",
)