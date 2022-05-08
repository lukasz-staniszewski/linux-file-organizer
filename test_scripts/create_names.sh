#!/bin/sh
mkdir -p ./X/X_1/X_2
touch ./X/first.txt
touch ./X/second.pl
touch ./X/X_1/third.c
touch ./X/X_1/X_2/fourth.py

echo first_X.txt > ./X/first.txt
echo second_X.pl > ./X/second.pl
echo third_X.c > ./X/X_1/third.c


mkdir -p ./Y1/Y1_1/
touch ./Y1/first.txt
touch ./Y1/Y1_1/fourth.py
echo first_Y1.txt > ./Y1/first.txt
echo fourth_Y1.py > ./Y1/Y1_1/fourth.py

mkdir -p ./Y2/Y2_1/
touch ./Y2/first.txt
touch ./Y2/Y2_1/fourth.py

mkdir -p ./Y3/Y3_1/Y3_2
touch ./Y3/Y3_1/Y3_2/first.txt
touch ./Y3/Y3_1/third.c
touch ./Y3/fifth.hpp

sleep 1
echo fourth_Y2.py > ./Y2/Y2_1/fourth.py
echo first_Y3.txt > ./Y3/Y3_1/Y3_2/first.txt
echo third_Y3.c > ./Y3/Y3_1/third.c

sleep 1
echo fourth_X.py > ./X/X_1/X_2/fourth.py
echo first_Y2.txt > ./Y2/first.txt
echo fifth_Y3.hpp > ./Y3/fifth.hpp