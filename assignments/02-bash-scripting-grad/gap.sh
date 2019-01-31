#!/usr/bin/env bash


DIR="../../data/gapminder/"

if [[ $# -eq 0 ]]; then 
	ls $DIR
	exit 
fi

FIRST_LETTER=${1^^}

if [[ $FIRST_LETTER == 'W' ]]; then
	echo "There are no countries starting with '$FIRST_LETTER'" 
	exit 1
fi
 
if [[ $FIRST_LETTER == 'w' ]]; then
        echo "There are no countries starting with '$FIRST_LETTER'"
        exit 1
fi

if [[ $FIRST_LETTER == 'X' ]]; then
	echo "There are no countries starting with '$FIRST_LETTER'" 
	exit 1
fi

if [[ $FIRST_LETTER == 'x' ]]; then
        echo "There are no countries starting with '$FIRST_LETTER'"
        exit 1
fi
find $DIR -name "$FIRST_LETTER*" -exec basename {} ';'

