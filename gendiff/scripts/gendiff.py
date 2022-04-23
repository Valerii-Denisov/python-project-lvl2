#!/usr/bin/env python
"""The main script of the project."""

import argparse as ap

from gendiff import generate_diff


def main():
    """Display info of package."""
    parser = ap.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='Set format of output: stylish, plain or json.',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
