#! /usr/bin/env sh

FILE1=$1

for FILE1 in "$@"
do
	wc $FILE1
done

echo $0
# Script with flag args using getopts

# :while getopts u:d:p:f: option
# do
# case "${option}"
# in
# u) USER=${OPTARG};;
# d) DATE=${OPTARG};;
# p) PRODUCT=${OPTARG};;
# f) FORMAT=${OPTARG};;
# esac
# done
# NVIDIA Tao NGC Mozilla Common voice Nvidia merlin, maxine, Triton(inference)
# NVIDIA Drive, AV, Orin, hyperion