#!/bin/sh
mkdir -p ./X/X_1/X_2
touch ./X/first.txt
touch ./X/second.pl
touch ./X/X_1/third.c
touch ./X/X_1/X_2/fourth.py

echo first.txt > ./X/first.txt
echo second.pl > ./X/second.pl
echo third.c > ./X/X_1/third.c
echo fourth.py > ./X/X_1/X_2/fourth.py

mkdir -p ./Y1/Y1_1/
touch ./Y1/first.txt
touch ./Y1/Y1_1/sixth.java
echo first.txt > ./Y1/first.txt
echo sixth.java > ./Y1/Y1_1/sixth.java

mkdir -p ./Y2/Y2_1/
touch ./Y2/seventh.hpp
touch ./Y2/Y2_1/eighth.xml
echo second.pl > ./Y2/seventh.hpp
echo eighth.xml > ./Y2/Y2_1/eighth.xml

mkdir -p ./Y3/Y3_1/Y3_2
touch ./Y3/Y3_1/Y3_2/third.c
echo new_third.c > ./Y3/Y3_1/Y3_2/third.c

