#!/bin/bash

function do_test {
  echo $'\n'$2$'\n'
  while read -r line ; do
    python3 ../script.py $line >/tmp/res
    printf "%-25s|" "$line"
    tail -2 /tmp/res | head -1
  done < $1
}

do_test test-file "These have a solution"
do_test test-one-away "These haven't got a solution, but are 1 away"
