#!/bin/bash

python2 insert_data.py gcc-x64/bulk_comparison_table.cpp.txt     README.md
python2 insert_data.py clang-x64/bulk_comparison_table.cpp.txt   README.md
python2 insert_data.py clang-arm64/bulk_comparison_table.cpp.txt README.md
python2 insert_data.py vs-x64/bulk_comparison_table.cpp.txt      README.md
python2 insert_data.py gcc-x86/bulk_comparison_table.cpp.txt     README.md
python2 insert_data.py clang-x86/bulk_comparison_table.cpp.txt   README.md
python2 insert_data.py vs-x86/bulk_comparison_table.cpp.txt      README.md
