#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2020-12-12
Purpose: Looking items up in a dictionary
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Looking items up in a dictionary',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs = "+",
                        help='A positional argument')

    parser.add_argument('-f',
                        '--file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    letter_dict = {}

    for line in args.file:
        letter_dict[line[0].upper()] = line.rstrip()
                    
    
    for letter in args.letter:
        if letter.upper() in letter_dict:
            print(letter_dict[letter.upper()]) 
        else:
            print(f'I do not know "{letter}".')


     # --------------------------------------------------
if __name__ == '__main__':
    main()
