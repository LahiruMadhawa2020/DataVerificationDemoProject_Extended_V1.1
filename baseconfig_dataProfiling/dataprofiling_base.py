import pandas as pd
import pandas_profiling
from datetime import datetime
import datetime
import os


class profilingBase:

    def __init__(self, dataframe_datasource, file_location1):
        self.df = dataframe_datasource
        self.file_location = file_location1

# To generate both html and json reports
    def sourcedataprofiling(self):
        # read only the file name except for path
        file_df = os.path.basename(self.file_location)
        # run the profile report
        profile = self.df.profile_report(title='Pandas Profiling Report {}'.format(file_df))
        # save the report as html file
        profile.to_file(output_file="reports/reports_profiling_html/pandas_profiling_report_for_{0}_{1}.html".format(file_df, datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
        # save the report as json file
        profile.to_file(output_file="reports/reports_profiling_json/pandas_profiling_report_for_{0}_{1}.json".format(file_df, datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))

# To generate only the html report
    def sourcedataprofilingjson(self):
        # read only the file name except for path
        file_df = os.path.basename(self.file_location)
        profile2 = self.df.profile_report(title='Two Pandas Profiling Report')
        # save the report as html file
        profile2.to_file(output_file="reports/reports_profiling_html/pandas_profiling_report_for_{0}_{1}.html".format(file_df, datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
        # save the report as json file
        # profile2.to_file(output_file="reports/reports_profiling_json/pandas_profiling_report_for_{0}_{1}.json".format(file_df, datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
