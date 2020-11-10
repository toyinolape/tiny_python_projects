#!/usr/bin/env python3
"""
Author: Toyin Olape <toyinolape"yahoo.com>
Purpose: Say Hello
"""

import argparse


def get_args():
    """ Get command line arguments"""

    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """ main """

    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == "__main__":
    main()
    