#!/usr/bin/env python3
"""
Author : toyin <toyinolape@yahoo.com>
Date   : 2020-11-29
Purpose: Word Count Exercise
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word Count Exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input files(s)',
                        metavar='FILE',
                        nargs="*",
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    tot_line, tot_words, tot_bytes = 0, 0, 0
    
    for fh in args.file:
        num_line, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_line += 1
            num_words += len(line.split())
            num_bytes += len(line)

        tot_line += num_line
        tot_words += num_words
        tot_bytes += num_bytes
        
        print(f'{num_line:8}{num_words:8}{num_bytes:8} {fh.name}')
        

    if len(args.file) > 1:
        print(f'{tot_line:8}{tot_words:8}{tot_bytes:8} total')

# --------------------------------------------------
if __name__ == '__main__':
    main()
