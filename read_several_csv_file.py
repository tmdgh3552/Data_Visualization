import csv

import glob

import os

import sys

input_path = "C:/Users/Haesung_public05/Desktop/test files/DATA SX NGÀY 14.01/DATA SX NG픜 14.01/TH01/CAV 1"

file_counter = 0

for input_file in glob.glob(os.path.join(input_path, '*.dat')):

    row_counter = 1

    with open(input_file, 'r', newline='') as csv_in_file:

        filereader = csv.reader(csv_in_file)

        header = next(filereader)

        for row in filereader:
            row_counter += 1

            print('{0!s}: ＼t{1:d} rows ＼t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))

            file_counter += 1

        print('Number of files: {0:d}'.format(file_counter))