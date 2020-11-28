#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2020-11-24
Purpose: Rock the Casbah
"""

import argparse
import io
import os 
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename (default: ',
                        metavar='text',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile( args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    print(args.text.upper(), file= out_fh)

# --------------------------------------------------
if __name__ == '__main__':
    main()
