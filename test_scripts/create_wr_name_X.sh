#!/bin/sh
mkdir -p ./X/X_1/X_2
touch ./X/good_1.txt
touch ./X/good_2.c
touch ./X/X_1/bad:1
touch ./X/X_1/X_2/b\"ad2
touch ./X/X_1/bd3.bd.pl
touch ./X/X_1/X_2/bad4\;.java
touch ./X/X_1/bd\?5bd.pl
touch ./X/X_1/X_2/bad6$.java
touch ./X/X_1/bd#7bd.pl
touch ./X/X_1/X_2/bad8\'.java
touch ./X/X_1/bd\|b9d.pl
touch ./X/X_1/X_2/ba10d\\.java
