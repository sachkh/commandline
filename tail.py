#!/usr/local/bin/python3.6

import sys
import os
import time


def tail(fname):
    '''
    :param fname: file path
    :return: line
    '''
    try:
        with open(fname) as fd:
            fd.seek(0, 2)
            for line in fd:
                if line:
                    yield line
                time.sleep(0.1)
    except:
        print('some error occurred')


if __name__ == '__main__':
    _, fname = sys.argv
    if not os.path.isfile(fname):
        print('No such file: {0}'.format(fname))
    tail(fname)