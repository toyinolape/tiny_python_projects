#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2020-12-13
Purpose: Find and Replace
"""

import argparse
import os
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find and Replace',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Inout text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type= str,
                        default="a",
                        choices=('aeiou'))

    args = parser.parse_args()

    if os.path.isfile( args.text):
        args.text = open(args.text).read().rstrip()

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []

    for words in text:
        if words in "aeiou":
            new_text.append(vowel)
        elif words in "AEIOU":
            new_text.append(vowel.upper())
        else:
            new_text.append(words)

    print("".join(new_text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
