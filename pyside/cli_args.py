#! /usr/bin/env python
# -*- coding:utf-8 -*-


import argparse

# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description="Process integers via CLI")
parser.add_argument(
    "integers",
    metavar="N",
    type=int,
    nargs="+",
    help="Hello try this integer accumulator"
)

parser.add_argument(
    "--sum",
    dest="accumulate",
    action="store_const",
    const=sum,
    default=max,
    help="sume the integers (default: find the max)"
)

args = parser.parse_args()
print(args.accumulate(args.integers))