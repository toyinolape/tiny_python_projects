#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2021-01-06
Purpose: Randomly mutating lists
"""

import argparse
import random
import os 
import sys
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Randomly mutating lists',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent Mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1 :
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile( args.text):
        args.text = open(args.text).read()

    return args 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    num_mutations = round(len(args.text) * args.mutations) # No of letters to mutate
    alpha = string.ascii_lowercase + string.punctuation 
    indexes = random.sample(list(range(len(args.text))), num_mutations) #Determine index of letters to mutate
    new_text = args.text
    
    for i in indexes:
        new_char = random.choice(alpha.replace(new_text[i],""))
        new_text = new_text[:i] + new_char + new_text[i + 1:] 


    print(f'You said: "{args.text}"\nI heard : "{new_text}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()