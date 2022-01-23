import os
from datetime import datetime
from typing import List
from pathlib import Path

import pandas as pd


def parse_input(input_file: str):
    # stores all the unique event types in the order as they appeared in the input
    unique_column_list = []
    # List of uniqueIds, event_type and event_time
    input_rows = []
    with open(input_file, "r") as f:
        # start file read from second line
        for line in f.readlines()[1:]:
            event_holder = []
            # splits input and stores in 3 variables
            unique_id, account_type, agg_val = line.split(",")
            # splits all events
            for event in agg_val.split("|"):
                # splits event_type and its time it appeared
                event_type, event_time = event.split("]")
                # convert string datetime into date object
                dt = datetime.strptime(event_time.strip("\n") + ":00", "%Y-%m-%d %H:%M:%S.%f%z")
                # convert date object into desired format eg. "Aug 08 2019, 04:12:53"
                fmt_dt = datetime.strftime(dt, "%b %d %Y, %H:%M:%S")
                # adds count of a column occurence as column suffix eg. "REGISTERED_1"
                unique_event_type = f"{event_type}_{event_holder.count(event_type)}"
                # stores column position as they appeared in the input file
                if unique_event_type not in unique_column_list:
                    unique_column_list.append(unique_event_type)
                event_holder.append(event_type)

                input_rows.append([unique_id, unique_event_type, fmt_dt])

    return input_rows, unique_column_list


def data_manipulator(df_input: List[List[str]], unique_column_list: List[str], output_file: str):
    df = pd.DataFrame(df_input, columns=['UniqueID', 'event_type', 'event_time'])
    new_df = df.pivot(index='UniqueID', columns='event_type', values='event_time')
    # pandas pivot alter the position of columns in the new dataframe, in order to keep them in order as they
    # first appeared in the input used df.reindex method with column names ordered in a list
    new_df.reindex(unique_column_list, axis=1).to_csv(output_file)


if __name__ == "__main__":

    output_file = os.getcwd() + "/source/CC_Application_Lifecycle_Output_1.csv"
    input_file = os.getcwd() + "/source/CC_Application_Lifecycle.csv"
    input_data, output_columns = parse_input(input_file)
    data_manipulator(input_data, output_columns, output_file)


