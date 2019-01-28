#!/bin/bash
read $1

if [[ $1 -z]]; then
        echo "Usage: cat-n.sh FILE"
exit

elif [[ -f "$1" ]]; then
        while read -r LINE; do
                echo $LINE
        done < "$FILE"
exit
else

echo "$1 is not a file"
exit
fi

6
