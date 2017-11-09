import sys
import os
from os.path import join, getsize
from collections import Counter


def get_files_list(dir_path):

    files_list = []

    for top, dirs, files in os.walk(dirpath):
        for the_name in files:
            full_filename = join(top, the_name)
            file_size = getsize(full_filename)
            files_list.append((the_name, file_size))

    return files_list


def get_duplicates(files_list):

    counted_files = Counter(files_list)

    duplicates = [file_counter[0] for file_counter in counted_files if file_counter[1] > 1]

    return duplicates


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('{} <filename>'.format(sys.argv[0]))

    dirpath = sys.argv[1]
    files_list = get_files_list(dirpath)

    duplicates_list = get_duplicates(files_list)

    for file, size in duplicates_list:
        print('{}   {}'.format(file, size))
