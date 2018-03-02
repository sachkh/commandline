#!/usr/local/bin/python3.6
import sys
import os


def read_file(fname):
    '''
    :param fname: file path
    :return: line from file
    '''
    try:
        with open(fname) as fd:
            for line in fd:
                yield line[:-1]
    except:
        print('some error occurred')


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print('Usage: python3.6 cat.py <file_path> ')
        return
    _, fname = sys.argv

    if not os.path.isfile(fname):
        print('No such file: ', fname)
        return
    for line in read_file(fname):
        print(line)


if __name__ == '__main__':
    main()
