#!/bin/bash
for i in 25 50 100 150 200 300 500 1000 1200
do 
echo '======================='$i'============='
echo '========================================'
bash scr1.sh $i
echo '========================================'
echo '========================================'
done
cp  -r results/* ../../visual/3_test
