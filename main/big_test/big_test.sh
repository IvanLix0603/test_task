#!/bin/bash
#echo "1_test:"
#cd 1_test
#bash scr2.sh
#bash ex.sh
#cd ..
#echo "2_test:"
#cd 2_test
#bash scr2.sh
#bash ex.sh
#cd ..
echo "3_test:"
cd 3_test
#bash ex.sh
bash scr2.sh 
cd ..
echo "4_test:"
cd 4_test
python3 thr.py
cd ..
