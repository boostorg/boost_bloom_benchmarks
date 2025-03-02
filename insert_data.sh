#!/bin/bash

python2 insert_data.py gcc-x64/comparison_table.cpp.txt     README.md
python2 insert_data.py clang-x64/comparison_table.cpp.txt   README.md
python2 insert_data.py clang-arm64/comparison_table.cpp.txt README.md
