# Read Editable PDF

This package provides a class `ReadEditablePDF` to extract text and coordinates from editable PDFs. The text can be extracted as individual words or as blocks of words (sentences). The extracted data is then saved to CSV files.

## Features

- **Extract Individual Words**: Extracts each word and its coordinates from the PDF.
- **Extract Word Blocks**: Extracts blocks of words (sentences) and their coordinates from the PDF.
- **Logging**: Uses a custom logger to log errors and important events.

## Project Structure

```
read_editable_pdf/
│
├── read_editable_pdf/
│   ├── __init__.py
│   ├── logger.py
│   ├── read_editable_pdf.py
│
├── logs/
│   ├── read_editable_pdf.log
│
├── README.md
├── setup.py
├── requirements.txt
└── MANIFEST.in
```


## Requirements

- `fitz` (PyMuPDF)
- `pandas`
- `logging`
- `os`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/harshad208/read_editable_pdf.git
    cd yourproject
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
   
## Usage

You can use the `ReadEditablePDF` class to extract text from a PDF and save it to CSV files. You need to provide the path for logging when creating an instance of the class.

### Example Script: How to Use as a Helper Method

**Example input**:

* pstr_pdf_file_path:- path/to/file.pdf
* output_put_file_path:- path/to/words.csv

lobj_pdf_reader = ReadEditablePDF(log_file_path)
lobj_pdf_reader.read_editable_pdf_words(pstr_pdf_file_path, output_put_file_path)
lobj_pdf_reader.read_editable_pdf_blocks(pstr_pdf_file_path, output_put_file_path)


