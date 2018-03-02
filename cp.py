#!/usr/local/bin/python3.6

import sys
import os


def open_src_file(src):
    """
    opens soure file and yields lines
    """
    with open(src, 'r') as f:
        for line in f:
            yield line


def copy(src, dest):
    """
    copy file function
    """
    try:
        filegen = open_src_file(src)
        fline = next(filegen)
        with open(dest, 'w') as fd:
            fd.write(fline)
            for line in filegen:
                fd.write(line)
    except FileNotFoundError:
        print('some error occured')


def main():
    """Main function"""
    if len(sys.argv) != 3:
        print('Usage: python3.6 cp.py <src_file_path> <destination_file_path>')
        return
    _, src, dest = sys.argv
    if not os.path.isfile(src):
        print('No such file or directory: ', src)
        return
    if src == dest:
        print('%s and %s are same files' % (src, dest))
        return
    copy(src, dest)


if __name__ == '__main__':
    main()

