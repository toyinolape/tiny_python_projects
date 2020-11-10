#!/usr/bin/env python3
"""
Author : toyin <toyin@localhost>
Date   : 2020-10-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic basket menu',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='food_items',
                        nargs="+",
                        help='Food items we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    food = args.items

    if args.sorted:
        food.sort()
    
        
    basket = ""
    
    if len(food) == 1:
        basket =  food[0]
        print(f"You are bringing {basket}.")
    elif len(food) == 2:
        basket = " and ".join(food)
        print(f"You are bringing {basket}.")
    else :
        food[-1] = "and "+ food[-1]
        basket = ", ".join(food)
        print(f"You are bringing {basket}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
