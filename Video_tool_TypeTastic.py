# TypeTastic - Python utility to make creating screencasts easier, and doing live demo's less stressful.

# PyPi: https://pypi.org/project/typetastic/

# pip install typetastic

# TypeTastic uses a Robot to type commands for you. In the simplest form you can pass the commands in as an array.
import typetastic


robot = typetastic.Robot()
robot.load(['ls', 'echo "Hello World\!"'])
robot.run()


# Something Useful
"""
tt-robot.py

# Run a typetastic command file.

# Usage:
   tt-robot.py <file>

import argparse
import typetastic


def main():
    """Run a typetastic file."""

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("inputfile")
    args = arg_parser.parse_args()

    robot = typetastic.Robot()
    robot.load(args.inputfile)
    robot.run()


if __name__ == "__main__":
    main()
"""

