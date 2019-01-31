#!/usr/bin/env bash


DIR="../../data/gapminder/"



FIRST_LETTER=$1

if [[ $# -gt 0]]; then 
	echo "hello" 
	exit 1
fi 
ls $DIR
