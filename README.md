# Beliveau_Remote

This repository holds the most important documents involving Jumana's Summer 2020 Project at the Beliveau Lab. More details can be found under the lab writeup included in this repository.

Both the prob project, as well as the cell profiler project writeups and relevant files can be found in this repository.

Job files are not included in this repo, but follow this general structure:
#!/bin/bash 
#$ -M jumanaf@uw.edu 
#$ -m abe  
#$ -e INSERT_ERROR_FILE.err
#$ -o INSERT_OUTPUT_FILE.out 

 
cd INSERT_FILE_ADDRESS 
python INSERT_PYTHON_SCRIPT.py
