#! /usr/bin/env sh

FILE1=$1

for FILE1 in "$@"
do
	wc $FILE1
done
