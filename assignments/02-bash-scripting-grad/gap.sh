#!/usr/bin/env bash


DIR="../../data/gapminder/"

if [[ $# -eq 0 ]]; then 
	ls $DIR
	exit 
fi

FIRST_LETTER=${1^^}

if [[ ! -z 'find $DIR -name "$FIRST_LETTER"' ]]; then 
	echo " There are no countries that start with '$FIRST_LETTER'"
	exit 1
fi
find $DIR -name "$FIRST_LETTER*" -exec basename {} ';' 


