#!/usr/bin/env python3.9

import sys
import shutil
import os
import pandas as pd

print("start of processing")
src = os.environ['INPUT_DIR']
dest = os.environ['OUTPUT_DIR']

print("Command line arguments ...")
print(sys.argv)
print("ENV variables ...")
print(os.environ)

# Customized Part of Echo to remove all rows with PatientID 'z'
print(f"Processing files from {src} and writing to {dest}")

files_to_process = ['df1.csv', 'df2.csv']
for filename in files_to_process:
    input_filepath = os.path.join(src, filename)
    output_filepath = os.path.join(dest, filename.replace('.csv', '_out.csv'))

    print(f"Reading input file: {input_filepath}")
    df = pd.read_csv(input_filepath)
    modified_df = df.loc[df['PatientID'] != 'z'].copy()

    print(f"Writing output file: {output_filepath}")
    modified_df.to_csv(output_filepath, index=False)

print("Files processed successfully.")

