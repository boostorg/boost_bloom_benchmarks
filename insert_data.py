# Feeds log data into md file
#
# Copyright 2022-2025 Joaquin M Lopez Munoz.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)
#
# See https://github.com/joaquintides/boost_bloom_benchmarks
# for project home page.

import argparse
import io
import re
import sys

parser=argparse.ArgumentParser(
    description="Feeds log data into md file for reporting")
parser.add_argument("input_file",help="txt file")
parser.add_argument("md_file",help="md file")
parser.add_argument("-e",dest="encoding",default=None,
  help="encoding (default none)")
args=parser.parse_args()

with io.open(args.input_file,"r",encoding=args.encoding) as input_file:
  lines=input_file.readlines()

md_delimiter="<!--"+args.input_file+"-->"
with open(args.md_file,"r") as md_file:
  md_out=re.sub(
    re.escape(md_delimiter)+r"(.|\n)*"+re.escape(md_delimiter),
    "{}\n{}\n{}".format(
      md_delimiter,
      "".join(lines),
      md_delimiter),
    md_file.read())

with open(args.md_file,"w") as md_file:
  md_file.write(md_out)
