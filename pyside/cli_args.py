#! /usr/bin/env python
# -*- coding:utf-8 -*-


import argparse
import textwrap

# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(
    prog='Valhalla',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''), 
    epilog='A bar that foos')
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


#######################################################
#    Using Cllick  for CLI apps
#####################################3################3

