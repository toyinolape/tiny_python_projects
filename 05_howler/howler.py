#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2020-11-17
Purpose: Howler Exercise
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler Exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()


    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    howler = args.text
    out_fh = open(args.outflie, "wt") if args.outfile else sys.stdout
    out_fh.write(howler.upper())
    out_fh.close()
     
# --------------------------------------------------
if __name__ == '__main__':
    main()
