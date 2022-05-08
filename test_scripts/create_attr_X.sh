#!/bin/sh
mkdir -p ./X/X_1/X_2
touch ./X/first.txt
touch ./X/second.c
touch ./X/X_1/third.cpp
touch ./X/X_1/X_2/fourth.py
touch ./X/X_1/fifth.sh
touch ./X/X_1/X_2/sixth.java

echo f > ./X/first.txt
echo s > ./X/second.c
echo t > ./X/X_1/third.cpp
echo f > ./X/X_1/X_2/fourth.py
echo f > ./X/X_1/fifth.sh
echo s > ./X/X_1/X_2/sixth.java

chmod 555 ./X/first.txt
chmod 777 ./X/second.c
chmod 000 ./X/X_1/third.cpp
chmod 077 ./X/X_1/X_2/fourth.py
chmod 111 ./X/X_1/fifth.sh
chmod 644 ./X/X_1/X_2/sixth.java
