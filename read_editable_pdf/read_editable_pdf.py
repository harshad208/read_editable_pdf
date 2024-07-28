import fitz
import pandas as pd
from logger import CustomLogger
import os


class ReadEditablePDF:
    def __init__(self, log_path:str):
        try:
            self.logger = CustomLogger.get_logger(__name__, log_path)
        except Exception as e:
            print(e)
            raise

    def read_editable_pdf_words(self, pstr_pdf_file_path: str, output_put_file_path: str):
        try:
            print("extracting individual words and their coordinates............")
            ldf_pdf_data = pd.DataFrame()
            if pstr_pdf_file_path != "":
                if os.path.exists(pstr_pdf_file_path):
                    list_dict_word_and_coordinates = list()
                    document = fitz.open(pstr_pdf_file_path)

                    # Iterate through each page and extract text and coordinates
                    for page_num in range(len(document)):
                        page = document.load_page(page_num)  # load page
                        blocks = page.get_text("words")  # extract text words
                        i = 1
                        for block in blocks:
                            x0, y0, x1, y1, text, _, _ , _ = block
                            ldict_temp = dict()
                            ldict_temp['id'] = i
                            ldict_temp['x0'] = x0
                            ldict_temp['y0'] = y0
                            ldict_temp['x1'] = x1
                            ldict_temp['y1'] = y1
                            ldict_temp['text'] = text
                            ldict_temp['page_number'] = page_num + 1
                            i= i + 1
                            list_dict_word_and_coordinates.append(ldict_temp)
                        ldf_pdf_data = pd.DataFrame(list_dict_word_and_coordinates)
                else:
                    print("file path does not exist")
            else:
                print("invalid file path for input!")

            ldf_pdf_data.to_csv(output_put_file_path)

        except Exception as e:
            self.logger.error(str(e), exc_info=True)
            raise

    def read_editable_pdf_blocks(self, pstr_pdf_file_path: str, output_put_file_path: str) -> pd.DataFrame():
        try:
            print("extracting individual word blocks and their coordinates............")
            ldf_pdf_data = pd.DataFrame()
            if pstr_pdf_file_path != "":
                if os.path.exists(pstr_pdf_file_path):
                    list_dict_word_and_coordinates = list()
                    document = fitz.open(pstr_pdf_file_path)

                    # Iterate through each page and extract text and coordinates
                    for page_num in range(len(document)):
                        page = document.load_page(page_num)  # load page
                        blocks = page.get_text("blocks")  # extract text words
                        i = 1
                        for block in blocks:
                            x0, y0, x1, y1, text, _, _ = block
                            ldict_temp = dict()
                            ldict_temp['id'] = i
                            ldict_temp['x0'] = x0
                            ldict_temp['y0'] = y0
                            ldict_temp['x1'] = x1
                            ldict_temp['y1'] = y1
                            ldict_temp['text'] = text
                            ldict_temp['page_number'] = page_num + 1
                            i= i + 1
                            list_dict_word_and_coordinates.append(ldict_temp)
                        ldf_pdf_data = pd.DataFrame(list_dict_word_and_coordinates)
                else:
                    print("file path does not exist")
            else:
                print("invalid file path for input!")

            ldf_pdf_data.to_csv(output_put_file_path)

        except Exception as e:
            self.logger.error(str(e), exc_info=True)
            raise
