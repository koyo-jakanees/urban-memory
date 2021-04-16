#!/usr/bin/env bash

# ref: https://www.learnshell.org/en/Basic_String_Operations
# ref: https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays
# ref: https://unix.stackexchange.com/questions/31414/how-can-i-pass-a-command-line-argument-into-a-shell-script
# ref: https://linuxize.com/post/bash-functions/
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

#  arrays in bash
new_array=()
new_array[0]="apple" 
new_array[1]="Maya"
new_array[2]="Banana"
new_array[4]="grapes"
new_array[5]="lemon"
new_array[6]="tomatoes"
new_array[7]="oranges"
new_array+=("apple" "Maya" "Banana" "grapes" "lemon" "tomatoes" "oranges")
echo "Elements of the new array: ${new_array[@]}"

echo "Using referencing: ${new_array[*]}"
new_array[2]=apricot

echo "after adding apricot: ${#new_array[@]}"
echo "last element is : ${new_array[${#new_array[@]}-3]}"

for i in ${new_array[@]}; do
    echo $i
done

#  operatons
# Basic operators on numbers
# a + b addition
# a - b substraction
# a * b multiplicaton
# a / b division
# a % b modulo(Integer remainder of a divided by b)
#  a ** b exponentiation

# String Operations.
#  string length

STRING="This is another useless string for demonstration"

echo "string length: ${#STRING}"

SUBSTRING="use"
expr index "$STRING" "$SUBSTRING"
# Extract substring of length $LEN from $STRING starting 
# after position $POS. Note that first position is 0.
# string slicing
POS=3
LEN=4
echo ${STRING:$POS:$LEN}
echo ${STRING:20}

# Data extract example
# extract the first name from the data record

DATARECORD="last=Clifford,first=Johnny Boy,state=CA"

COMMA1=`expr index "$DATARECORD" ','` # 14 position of the first comma
CHOPFIELD=${DATARECORD:$COMMA1}
COMMA2=`expr index "$CHOPFIELD" ','`
LENGTH=`expr $COMMA2 - 6 - 1`
FIRSTNAME=${CHOPFIELD:6:LENGTH}

echo "Alllaaaa"
echo $FIRSTNAME

# Substring replacement
# replaces the first occurrance with replacement
echo "Before replacement"

echo $STRING

echo "After replacement"
echo ${STRING[@]/another/obnoxious}

# delete all occurrences{replaces with an empty string}

REP="Hello from the otherside fellas whooo whoo"
echo $REP

echo "After deleting whoo whoo"
echo ${REP[@]// whooo}

# Replace occurrences of substring if at the beginning of $REP
echo ${REP[@]/#Hello/this side}

# Replace occurrence of substring at the end of $STRING
echo ${REP[@]/%whoo/$(date +%Y-%M-%d)}
echo "return status: $?"
# Logical decision making construct
# if [expression]; then 
#     do something
# fi

NAME="John"
if [ "$NAME" = "John" ]; then
    echo "True that my name is Indeed $NAME"
    # expand using an else expression
else
    echo "Sorry Wrong"
    echo "My name is actually Bill"
fi

# further using 'elif expansion'
NAME=$5
if [ "$NAME" = "John" ]; then
    echo "True that my name is Indeed $NAME"
    # expand using an else expression
elif [ "$NAME" = "Deil" ]; then
    echo "True That, I am Gloria ${NAME}"
else
    echo "Sorry Wrong"
    echo "This leaves us with Akwabba"
fi

# Types of Numeric comparisons
# ------------------------------- #
# comparison  Evaluated to true when
# $a -lt $b     $a < $b
# $a -gt $b     $a > $b
# $a -le $b     $a <= $b
# $a -ge $b     $a >= $b
# $a -eq $b     $a == $b
# $a -ne $b     $a != $b
# 
# String comparisons
# ----------------------------------- #
# "$a" = "$b"    $a is the same as $b
# "$a" == "$b"   $a is the same as $b
# "$a" != "$b"   $a is different from $b
# -z "$a"        $a is empty
# 
# note:   whitespace around `=` is required
        # use "" double quotes around string variables to avoid
        # shell expansion of special characters as *
# 
# Logical combinations
# ------------------------------------- #
# if <a href='/en/_%24VAR_A_-eq_1_%26%26_%28%24VAR_B_%3D_%22bee%22_'>| $VAR_T = "tee") </a> ; then
    # command. here..
# fi
# 
# Case Structure
# -------------------------------------- #
# case "$variable" in
    # "$condition1" )
        # command...
    # ;;
    # "$condition2" )
        # command...
    # ;;
# esac