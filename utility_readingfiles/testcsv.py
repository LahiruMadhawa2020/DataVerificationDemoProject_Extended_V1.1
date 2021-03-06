import pandas as pdf
from utility_readingfiles.localfilereader import LocalFileReader
from utility_readingfiles.flattningfiles import FlatteningFiles
from io import StringIO


class Testcsv(FlatteningFiles):

    test_date = None

    def convert_to_pdf(self, **kwargs):

        csv_content_list = LocalFileReader().read_csv("input_filerepository/csv")
        utility = kwargs.get("utils")
        # print("---------------1--------------")
        # print(utility.month)
        # print(utility.was_bucket)
        # print("---------------2--------------")
        Testcsv.test_date = pdf.read_csv(StringIO(csv_content_list), sep=","
                                                           , skip_blank_lines=True, header=0)  # convert string to pandas data frame


