#!/usr/bin/env sh

ps | grep $$

echo "I am using: $SHELL"

greeting="Hello     World!"
# variables usage

price_per_apple=10
firstletters=ABCDE
echo "the price of an Apple today is \$HK $price_per_apple"
echo "the first 10 letters of the alphabet are: ${firstletters}FGHIJ"
echo $greeting" now with spaces: $greeting"

echo $greeting
echo "today is : $(date -d "$date1" +%A)"

FILELIST=`ls`
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%d).txt

# Passing arguments to your script
echo "The first fruit is: $1"
echo "The second fruit is: $2"
echo "The third fruit is: $3"

echo "All fruits are: $@"

echo "Number of Args passed: $#"

FILE=$4
countNumber=`wc $FILE`

echo "word count \n $countNumber"
